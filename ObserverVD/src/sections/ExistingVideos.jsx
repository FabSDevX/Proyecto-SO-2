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
import propTypes from "prop-types";

export function ExistingVideos({ handleVideoData, activateDrop }) {
  const [storageBlob, setStorageBlob] = useState(null);
  const [showData, setShowData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [nullIndex, setNullIndex] = useState(0);
  const [selectedCard, setSelectedCard] = useState(null);

  useEffect(() => {
    setLoading(true);
    setStorageBlobData();
  }, []);
  
  useEffect(() => {
    setSelectedCard(null);
  }, [activateDrop]);

  useEffect(() => {
    if (storageBlob && storageBlob["count"] > 0) {
      setMovieVideoData();
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
    setNullIndex(results.filter((result) => result == null).length);
    setShowData(results.filter((result) => result != null));
    setLoading(false);
  }

  const handleCardClick = (index) => {
    const isSelected = selectedCard === index;
    setSelectedCard(isSelected ? null : index);
    if(index!=0){
      handleVideoData(isSelected ? null : storageBlob.blobs[index + nullIndex]);
    }
    else{
      handleVideoData(isSelected ? null : storageBlob.blobs[index]);
    }
  };

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
            <Card
              className={`card-video ${
                selectedCard === index ? "selected" : ""
              }`}
              sx={{ maxWidth: 345 }}
              key={index}
              onClick={() => handleCardClick(index)}
            >
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

ExistingVideos.propTypes = {
  handleVideoData: propTypes.any,
  activateDrop: propTypes.any,
};
