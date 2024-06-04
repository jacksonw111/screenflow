import { useGlobalStore } from "@/stores/useGlobalStore";
import { LogoutOutlined } from "@ant-design/icons";

const Logout = () => {
  const { clean } = useGlobalStore();
  return (
    <div className="mb-8">
      <LogoutOutlined onClick={clean} className=""/>
    </div>
  );
};
export default Logout;
