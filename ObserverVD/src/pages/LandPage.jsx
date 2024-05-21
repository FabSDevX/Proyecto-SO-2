import { CopyrightFooter } from "../sections/CopyrightFooter";
import { Hero } from "../sections/Hero";
import { FileDrag } from "../sections/FileDrag";
import { useEffect } from "react";
import HeroImg from "@assets/svg/hero.svg";
import { askNotificationPermission } from "../utils/notifications/notification";
import { AvatarCards } from "../sections/AvatarCards";
import { ExistingVideos } from "../sections/ExistingVideos";
import { useState } from "react";
export function LandPage() {
  const [selectActor, setSelectActor] = useState(null);
  const handleActorData = (data) => {
    setSelectActor(data);
  };

  useEffect(() => {
    askNotificationPermission();
  }, []);

  useEffect(() => {
    console.log(selectActor);
  }, [selectActor]);
  return (
    <>
      <div>
        <Hero
          title={
            "Analizador de videos especializado en peliculas para detección de apariciones de objetos y famosos"
          }
          paragraph={
            "Detecta objetos especificos y actores famosos con nuestra inteligencia artificial entrenada para encontrarlo en tu video y mostrar cuantas apariciones ha tenido a lo largo de la duración del contenido"
          }
          image={HeroImg}
        />
        <AvatarCards handleActorData={handleActorData} />
        <FileDrag selectedActor={selectActor} />
        <ExistingVideos />
        <CopyrightFooter />
      </div>
    </>
  );
}
