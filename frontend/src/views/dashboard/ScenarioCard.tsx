import { AnimatedNumber } from "@/components/AnimateNumber";
import { Card } from "antd";
import { useEffect, useState } from "react";

const ScenarioCard = () => {
  const [count, setCount] = useState(0);
  useEffect(() => {
    setTimeout(() => {
      setCount(10000);
    }, 500);
  }, []);
  return (
    <Card className="card w-full h-full shadow-2xl">
      <div className="uppercase">Scenario</div>
      <div className="w-full h-full grow flex items-center justify-center font-extrabold text-6xl">
        <AnimatedNumber value={count} />
      </div>
    </Card>
  );
};
export default ScenarioCard;
