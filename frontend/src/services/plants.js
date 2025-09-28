import api from "./api";

export const getPlants = async () => {
  const res = await api.get("/plants");
  return res.data;
};

export const createPlant = async (plant) => {
  const res = await api.post("/plants", plant);
  return res.data;
};
