import api from "./api";

export const getGardens = async () => {
  const res = await api.get("/gardens");
  return res.data;
};

export const createGarden = async (garden) => {
  const res = await api.post("/gardens", garden);
  return res.data;
};
