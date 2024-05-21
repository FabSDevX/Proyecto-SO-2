import { SERVER_IP } from "../../data/general";

export async function uploadBlob(file: File) {
  try {
    const formData = new FormData();
    formData.append("file", file);
    const response = await fetch(`${SERVER_IP}/upload`, {
      method: "POST",
      body: formData,
    });
    if (response.ok) {
      return true;
    }
    return false;
  } catch (error) {
    console.error("Upload error request", error);
  }
}
