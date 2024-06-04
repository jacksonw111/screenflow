import { project_service } from "@/services/project";
import {
  keepPreviousData,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { Pagination } from "antd";
import { m } from "framer-motion";
import { useEffect, useState } from "react";

const ProjectList = () => {
  const queryClient = useQueryClient();

  const [page, setPage] = useState({
    current_page: 0,
    page_size: 10,
  });

  const { status, data, error, isFetching, isPlaceholderData } = useQuery({
    queryKey: ["projects", page],
    queryFn: () => project_service.get_all(page),
    placeholderData: keepPreviousData,
    staleTime: 5000,
  });

  useEffect(() => {
    if (
      !isPlaceholderData &&
      data?.total &&
      data?.total > (page.current_page + 1) * page.page_size
    ) {
      queryClient.prefetchQuery({
        queryKey: ["projects", page],
        queryFn: () =>
          project_service.get_all({
            ...page,
            current_page: page.current_page + 1,
          }),
      });
    }
  }, [data, isPlaceholderData, page, queryClient]);

  return (
    <div className="flex flex-col gap-3 w-full">
      <div className="w-full h-full grid grid-cols-4 gap-10 p-3 grow">
        {data?.projects.map((project) => (
          <m.div
            whileHover={{ scale: 1.1 }}
            key={project.id}
            className="card shadow-lg cursor-pointer"
          >
            <div className="card-body">
              <div className="card-title">{project.name}</div>
              <p>{project.description}</p>
            </div>
          </m.div>
        ))}
      </div>
      <div className="flex items-center justify-end">
        <Pagination
          current={page.current_page + 1}
          pageSize={page.page_size}
          total={data?.total}
          onChange={(current_page) =>
            setPage({
              ...page,
              current_page: current_page - 1,
            })
          }
        />
      </div>
    </div>
  );
};
export default ProjectList;
