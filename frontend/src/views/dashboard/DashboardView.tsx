import Main from "@/components/Main";
import ProjectCard from "./ProjectCard";
import ScenarioCard from "./ScenarioCard";

const DashboardView = () => {
  return (
    <Main>
      <div className="h-48 grid grid-cols-3 gap-3">
        <ProjectCard />
        <ScenarioCard />
        <ProjectCard />
      </div>
    </Main>
  );
};
export default DashboardView;
