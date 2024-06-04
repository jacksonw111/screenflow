import clsx from "clsx";
import { m } from "framer-motion";
import { ComponentProps, FC } from "react";

const Main: FC<ComponentProps<"div">> = ({ children, className }) => {
  return (
    <m.div
      initial={{ opacity: 0, y: -500 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 500 }}
      className={clsx(
        "w-full h-full bg-white rounded-lg p-3 overflow-scroll shadow-xl",
        className
      )}
    >
      {children}
    </m.div>
  );
};
export default Main;
