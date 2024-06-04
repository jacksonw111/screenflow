import { StyleProvider } from "@ant-design/cssinjs";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ConfigProvider, Flex } from "antd";
import { AnimatePresence } from "framer-motion";
import React, { Suspense } from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import MotionLazy from "./components/MotionLazy.tsx";
import SimpleLoading from "./components/SimpleLoading.tsx";
import "./index.css";

// 创建一个 client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 3, // 失败重试次数
      staleTime: 10_1000, // 数据变得 "陈旧"（stale）的时间 10s
      refetchOnWindowFocus: false, // 禁止窗口聚焦时重新获取数据
      refetchOnReconnect: false, // 禁止重新连接时重新获取数据
      refetchOnMount: false, // 禁止组件挂载时重新获取数据
    },
  },
});

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ConfigProvider
      theme={{
        components: {
          Menu: {
            // itemHoverBg: "#FF7F33",
            // colorPrimary: "#FF7F64",
            // colorPrimaryBorder: "#FF7F64",
            // collapsedIconSize: 20,
          },
        },
      }}
    >
      <QueryClientProvider client={queryClient}>
        <Suspense
          fallback={
            <Flex
              vertical
              align="center"
              justify="center"
              className="w-screen h-screen opacity-60 z-10"
            >
              <SimpleLoading />
            </Flex>
          }
        >
          <MotionLazy>
            <StyleProvider layer>
              <AnimatePresence>
                <App />
              </AnimatePresence>
            </StyleProvider>
          </MotionLazy>
        </Suspense>
      </QueryClientProvider>
    </ConfigProvider>
  </React.StrictMode>
);
