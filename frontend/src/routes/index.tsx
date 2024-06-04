import Layout from "@/layout/Layout";
import { useGlobalStore } from "@/stores/useGlobalStore";
import { auth_service } from "@/utils/auth";
import { lazy } from "react";
import { createBrowserRouter } from "react-router-dom";
const create_router = () =>
  createBrowserRouter([
    {
      path: "/login",
      Component: lazy(() => import("@/views/login/LoginView")),
    },
    {
      path: "/logout",
      action: async () => {
        auth_service.logout().then(() => {
          useGlobalStore.getState().clean();
        });
      },
    },
    {
      path: "/",
      Component: Layout,
      children: [
        {
          path: "dashboard",
          Component: lazy(() => import("@/views/dashboard/DashboardView")),
        },
        {
          path: "user",
          Component: lazy(() => import("@/views/user/UserView")),
        },
        {
          path: "project",
          Component: lazy(() => import("@/views/project/ProjectView")),
        },
        {
          path: "setting",
          Component: lazy(() => import("@/views/setting/SettingView")),
        },
      ],
    },
  ]);

export const router = create_router();
