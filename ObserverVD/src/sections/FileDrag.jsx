import "./FileDrag.css";
import { useCallback, useState } from "react";
import upload from "../assets/webp/upload.webp";
import { useDropzone } from "react-dropzone";
import { useNavigate } from "react-router-dom";
import { uploadBlob } from "../utils/apis/postApi";
import propTypes from "prop-types";
import { useEffect } from "react";
import { CircularProgress } from "@mui/material";

export function FileDrag({ selectedActor, handleVideoData, selectedVideoParam, handleDrop }) {
  const [navigated, setNavigated] = useState(false);
  const [loading, setLoading] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const [selectedVideo, setSelectedVideo] = useState(selectedVideoParam);

  const navigate = useNavigate();

  function navigateToReports() {
    if (!navigated) {
      if (selectedActor == null) {
        alert("Selecciona a un actor!");
      } else {
        setNavigated(true);
        navigate("/reports", {
          state: {
            selectedVideo,
            selectedActor,
          },
        });
      }
    }
  }

  useEffect(() => {
    if(selectedVideoParam==null){
      setLoaded(false);
    }
    setSelectedVideo(selectedVideoParam)
  },[selectedVideoParam]);

  useEffect(()=>{
    handleChange();
  },[selectedVideo])

  function handleChange(){
    if(selectedVideo!=null){
      setLoading(false);
      setLoaded(true);
      setSelectedVideo(selectedVideo);
      handleDrop(false);
      handleVideoData(selectedVideo)
    }
  }

  const onDrop = useCallback(async (acceptedFiles) => {
    setLoaded(false);
    setLoading(true);
    handleDrop(true);
    const acceptedVideoFormats = ["mp4", "mp3", "avi", "mkv"];
    acceptedFiles = acceptedFiles[0];
    const name = acceptedFiles["name"];
    const parts = name.split(".");
    const size = parts.length;
    if (acceptedVideoFormats.includes(parts[size - 1])) {
      await uploadBlob(acceptedFiles);
      setLoading(false);
      setLoaded(true);
      setSelectedVideo(name);
      handleVideoData(name)
    } else {
      alert("Formato no aceptado");
    }
  }, []);

  /*Props of Dropzone dependency*/
  const { getRootProps, getInputProps, isDragActive, open } = useDropzone({
    onDrop,
    noClick: true,
    multiple: false, //Just one video or movie
  });

  return (
    <>
      <section className="dg-container">
        {window.innerWidth >= 600 ? (
          <label className="dg-title">Subir o arrastrar el archivo</label>
        ) : (
          <label className="dg-title">Subir el archivo</label>
        )}
        <div
          className="dg-actor"
          {...getRootProps()}
          onClick={(event) => event.stopPropagation()}
        >
          <input {...getInputProps({ multiple: true })} />
          {isDragActive ? (
            <img className="dg-img" src={upload} alt="upload img" />
          ) : (
            <button type="button" className="dg-button" onClick={open}>
              Subir Archivo
            </button>
          )}
        </div>
        <span className="dg-span-note">
          Formatos aceptados son .mp4, .mp3, .avi, .mkv
        </span>

        {loading ? (
          <><p>Cargando archivos...</p><CircularProgress /></>
        ) : (
          loaded && (
            <>
              <button className="FileDrag-btn" onClick={navigateToReports}>
                Procesar
              </button>
              <div className="selected-video">
                <span className="first-span">
                Video seleccionado: 
                </span>
                <span className="second-span">
                   {selectedVideo}
                </span>
              </div>
            </>
          )
        )}
      </section>
    </>
  );
}

FileDrag.propTypes = {
  selectedActor: propTypes.any,
  handleVideoData: propTypes.any,
  selectedVideoParam: propTypes.any,
  handleDrop: propTypes.any
};
