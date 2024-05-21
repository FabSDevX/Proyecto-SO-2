import "./FileDrag.css";
import { useCallback, useState } from "react";
import upload from "../assets/webp/upload.webp";
import { useDropzone } from "react-dropzone";
import { useNavigate } from "react-router-dom";
import { uploadBlob } from "../utils/apis/postApi";
import propTypes from "prop-types";

export function FileDrag({ selectedActor }) {
  const [navigated, setNavigated] = useState(false);
  const [loading, setLoading] = useState(false);
  const [loaded, setLoaded] = useState(false);
  
  const navigate = useNavigate();

  function navigateToReports() {
    if (!navigated) {
      if (selectedActor == null) {
        alert("Selecciona a un actor!");
      } else {
        setNavigated(true);
        navigate("/reports", {
          state: {},
        });
      }
    }
  }

  const onDrop = useCallback((acceptedFiles) => {
    const acceptedVideoFormats = ["mp4", "mp3", "avi", "mkv"];
    acceptedFiles = acceptedFiles[0];
    const name = acceptedFiles["name"];
    const parts = name.split(".");
    const size = parts.length;
    if (acceptedVideoFormats.includes(parts[size - 1])) {
      setLoading(true);
      const response = uploadBlob(acceptedFiles);
      if (response) {
        setLoading(false);
        setLoaded(true);
      } else {
        alert("Error subiendo el archivo");
      }
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
          <p>Cargando archivos...</p>
        ) : (
          loaded && (
            <button className="FileDrag-btn" onClick={navigateToReports}>
              Procesar
            </button>
          )
        )}
      </section>
    </>
  );
}

FileDrag.propTypes = {
  selectedActor: propTypes.any,
};
