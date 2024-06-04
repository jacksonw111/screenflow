import api from "@/utils/http";

export interface ProjectRequest {
  name: string;
  description?: string;
}

export interface ProjectResponse {
  id: string;
  name: string;
  description?: string;
}

class ProjectService {
  url = "/api/projects";
  async get_all(params: {
    name?: string;
    current_page: number;
    page_size: number;
  }): Promise<{
    total: number;
    projects: ProjectResponse[];
  }> {
    const { data } = await api.get(this.url, { params });
    return data;
  }

  async create(project: ProjectRequest) {
    await api.post(this.url, project);
  }

  async update(project_id: string, project: ProjectRequest) {
    await api.put(`${this.url}/${project_id}`, project);
  }

  async remove(project_id: string) {
    await api.delete(`${this.url}/${project_id}`);
  }
}

export const project_service = new ProjectService();
