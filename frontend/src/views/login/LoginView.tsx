import hiImg from "@/assets/hi.svg";
import LoginImage from "@/assets/login.svg";
import { useGlobalStore } from "@/stores/useGlobalStore";
import { auth_service } from "@/utils/auth";

import { LockOutlined, MailOutlined } from "@ant-design/icons";
import { Button, Form, message } from "antd";
import { m } from "framer-motion";
import { Navigate, useNavigate } from "react-router-dom";
const LoginView = () => {
  const [form] = Form.useForm<{
    email: string;
    password: string;
  }>();
  const navigate = useNavigate();
  const { access_token, setToken, setRefreshToken } = useGlobalStore();
  if (access_token) return <Navigate to={"/dashboard"} />;
  const onFinish = (values: { email: string; password: string }) => {
    form.validateFields();
    auth_service.get_access_token(values.email, values.password).then((res) => {
      setToken(res.access_token);
      setRefreshToken(res.refresh_token);
      message.success("login successful");
      navigate("/");
    });
  };
  return (
    <div className="flex w-screen h-screen overflow-hidden">
      <div className="w-1/2 h-full flex flex-col items-center justify-center gap-10">
        <div className="w-1/2  flex items-center justify-start gap-3">
          <img src={hiImg} alt="" className="w-16" />
          <m.span
            initial={{ y: -500, rotate: 3 }}
            animate={{ y: 0 }}
            className="font-bold text-4xl p-2"
          >
            welcome back
          </m.span>
        </div>
        <Form className="flex flex-col w-1/2" form={form} onFinish={onFinish}>
          <Form.Item name="email" required>
            <label
              htmlFor="email"
              className="input input-bordered flex gap-3 items-center justify-start"
            >
              <MailOutlined />
              <input
                placeholder="email"
                type="text"
                name="email"
                className="w-full p-2 rounded"
              />
            </label>
          </Form.Item>
          <Form.Item name="password" required>
            <label
              htmlFor="password"
              className="input input-bordered flex gap-3 items-center justify-start"
            >
              <LockOutlined />
              <input
                placeholder="password"
                type="password"
                name="password"
                className="w-full p-2 rounded"
              />
            </label>
          </Form.Item>
          <Button htmlType="submit" className="btn btn-primary">
            Login
          </Button>
        </Form>
      </div>
      <div className="w-1/2 h-full bg-orange-50">
        <img src={LoginImage} />
      </div>
    </div>
  );
};
export default LoginView;
