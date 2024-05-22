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


export async function processVideo(actorName: string, videoName: string) {
  try {
    const formData = new FormData();
    formData.append("url_pelicula", "https://describedmovies.blob.core.windows.net/uploaded-movies/"+videoName);
    formData.append("name", actorName);
    const response = await fetch(`${SERVER_IP}/procesar_pelicula`, {
      method: "POST",
      body: formData,
    });
    if (response.ok) {
      return response.json();
    }
    return null;
  } catch (error) {
    console.error("Upload error request", error);
  }
}

