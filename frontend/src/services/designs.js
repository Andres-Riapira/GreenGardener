import api from "./api";

export const getDesigns = async () => {
  const res = await api.get("/designs");
  return res.data;
};

export const createDesign = async (design) => {
  const res = await api.post("/designs", design);
  return res.data;
};
