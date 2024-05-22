import { SERVER_IP } from "../../data/general";

export async function getStorageElements() {
  try {
    const response = await fetch(`${SERVER_IP}/obtener_elementos`, {
      method: "GET",
    });
    if (response.ok) {
      return await response.json();
    }else {
      throw new Error(`Request failed with status ${response.status}`);
    }
  } catch (error) {
    console.error("Process request error:", error);
  }
}

async function searchMovie(name: string | number | boolean) {
  try {
    const response = await fetch(`${SERVER_IP}/search_movie?name=${encodeURIComponent(name)}`, {
      method: "GET",
    });
    if (response.ok) {
      return await response.json();
    } else {
      // console.error(`Error fetching data for ${name}:`, response.statusText);
      return null;
    }
  } catch (error) {
    console.error(`Request error for ${name}:`, error);
    return null;
  }
}

export async function searchMovies(names: any[]) {
  try {
    const promises = names.map((name: any) => searchMovie(name));
    const results = await Promise.all(promises);
    return results;
  } catch (error) {
    console.error("Error processing movie search requests:", error);
    return [];
  }
}