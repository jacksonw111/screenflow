import { router } from "@/routes";
import { useGlobalStore } from "@/stores/useGlobalStore";
import { auth_service } from "@/utils/auth";
import axios, {
  AxiosError,
  AxiosRequestConfig,
  AxiosResponse,
  InternalAxiosRequestConfig,
} from "axios";

export interface HttpResponse<T = unknown> {
  status: number;
  msg: string;
  code: number;
  data: T;
}

export interface ErrorResponse<T = unknown> {
  response: {
    data: T;
  };
}

const config: AxiosRequestConfig = {
  baseURL: import.meta.env.BASE_URL,
  timeout: 60000,
  headers: {
    "Content-Type": "application/json",
  },
};

const api = axios.create(config);
api.interceptors.request.use(
  (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig => {
    if (config.url?.includes("download")) {
      config.responseType = "blob";
    }
    const { access_token } = useGlobalStore.getState();
    if (access_token) {
      config.headers.Authorization = `Bearer ${access_token}`;
    }

    return config;
  },
  (err: AxiosError) => {
    console.error(err);
    return Promise.reject(err);
  }
);

/**
 * 返回
 */
api.interceptors.response.use(
  (response: AxiosResponse<HttpResponse>) => {
    const res = response;
    const url = response.config.url;
    if (url?.includes("download")) {
      response.headers.responseType = "blob";
    }
    return res;
  },
  (error: AxiosError) => {
    console.error(error);
    const { config, status } = error?.response || {};

    if (status === 401) {
      const { access_token, refresh_token, setToken, setRefreshToken, clean } =
        useGlobalStore.getState();
      if (refresh_token && access_token) {
        auth_service
          .get_refresh_token(refresh_token, access_token)
          .then((res) => {
            setRefreshToken(res.refresh_token);
            setToken(res.access_token);
            api(config!);
          })
          .catch((e) => {
            clean();
            router.navigate("/login", { replace: true });
            return Promise.resolve([true, e?.response?.data]);
          });
      }
    }

    return Promise.resolve([true, error?.response?.data]);
  }
);

export default api;
