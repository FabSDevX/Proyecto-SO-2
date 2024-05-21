import { useEffect, useState } from "react";
import { getStorageElements, searchMovies } from "../utils/apis/getApi";
import {
  Card,
  CardActionArea,
  CardContent,
  CardMedia,
  CircularProgress,
  Typography,
} from "@mui/material";
import "./ExistingVideos.css";

export function ExistingVideos() {
  const [storageBlob, setStorageBlob] = useState(null);
  const [showData, setShowData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    setStorageBlobData();
  }, []);

  useEffect(() => {
    if (storageBlob && storageBlob["count"] > 0) {
      // setMovieVideoData();
    } else if (storageBlob) {
      setLoading(false);
    }
  }, [storageBlob]);

  async function setStorageBlobData() {
    const data = await getStorageElements();
    setStorageBlob(data);
  }

  async function setMovieVideoData() {
    const results = await searchMovies(storageBlob["blobs"]);
    setShowData(results);
    setLoading(false);
  }

  return (
    <section className="existing-videos">
      <h2>Analiza los videos/peliculas subidas por los demás usuarios</h2>
      <div id="showMoviesVideos">
        {loading ? (
          <div className="loading">
            <CircularProgress />
            <Typography variant="h6" color="text.secondary">
              Cargando contenido...
            </Typography>
          </div>
        ) : showData && showData.length > 0 ? (
          showData.map((video, index) => (
            <Card className="card-video" sx={{ maxWidth: 345 }} key={index}>
              <CardActionArea>
                <CardMedia
                  component="img"
                  height="500px"
                  image={video.poster_url}
                  alt={video.title}
                />
                <CardContent>
                  <Typography gutterBottom variant="h5" component="div">
                    {video.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {video.description}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          ))
        ) : (
          <div className="noContent">
            <Typography variant="h6" color="text.secondary">
              <p>No hay contenido disponible.</p>
            </Typography>
          </div>
        )}
      </div>
    </section>
  );
}
