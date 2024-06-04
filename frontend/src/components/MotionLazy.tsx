import { LazyMotion, domMax, m } from "framer-motion";
import { FC, PropsWithChildren } from "react";

const MotionLazy: FC<PropsWithChildren> = ({ children }) => {
  return (
    <LazyMotion features={domMax}>
      <m.div className="w-full h-full">{children}</m.div>
    </LazyMotion>
  );
};
export default MotionLazy;
