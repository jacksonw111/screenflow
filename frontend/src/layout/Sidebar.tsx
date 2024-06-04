import rocket from "@/assets/rocket.svg";
import {
  DashboardOutlined,
  ProjectOutlined,
  SettingOutlined,
  UserOutlined,
} from "@ant-design/icons";
import clsx from "clsx";
import { NavLink } from "react-router-dom";
import Logout from "./Logout";
const items = [
  {
    path: "/dashboard",
    icon: <DashboardOutlined />,
  },
  {
    path: "/project",
    icon: <ProjectOutlined />,
  },
  {
    path: "/user",
    icon: <UserOutlined />,
  },
  {
    path: "/setting",
    icon: <SettingOutlined />,
  },
];
const Sidebar = () => {
  return (
    <div className="w-20 h-screen flex items-center justify-center flex-col gap-5">
      <div className="h-16 p-3 text-3xl font-extrabold rotate-45">
        <img src={rocket} />
      </div>
      <div className="grow flex flex-col gap-3 items-center justify-start">
        {items.map((item) => (
          <NavLink
            to={item.path}
            className={({ isActive }) =>
              clsx(
                "hover:bg-slate-100 p-3 rounded-xl w-16 flex items-center justify-center",
                isActive && "bg-slate-100"
              )
            }
          >
            {item.icon}
          </NavLink>
        ))}
      </div>
      <div>
        <Logout />
      </div>
    </div>
  );
};
export default Sidebar;
