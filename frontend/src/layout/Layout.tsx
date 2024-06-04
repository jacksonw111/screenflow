import { useGlobalStore } from "@/stores/useGlobalStore";
import { Navigate, Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";

const Layout = () => {
  const { access_token } = useGlobalStore();
  if (!access_token) return <Navigate to="/login" />;
  return (
    <div className="w-screen h-screen flex">
      <Sidebar />
      <div className="w-screen h-screen bg-slate-100 p-3">
        <Outlet />
      </div>
    </div>
  );
};
export default Layout;
