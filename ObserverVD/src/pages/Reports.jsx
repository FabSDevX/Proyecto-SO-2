import { Hero } from "../sections/Hero";
import { CopyrightFooter } from "../sections/CopyrightFooter";
import { Stats } from "../sections/Stats";
import HeroImg from "@assets/svg/hero.svg";
export function Reports() {
  return (
    <>
      <div style={{ minWidth: "622px" }}>
        <Hero
          title={"Reportes del detector"}
          paragraph={
            "A continuación se muestran los resultados del analisis del detector de objetos y actores o famosos con el fin de ver cuantas apariciones tienen los cuchillos y lentes en el video. Igualmente el famoso seleccionado"
          }
          image={HeroImg}
        />
        <Stats />
        <CopyrightFooter /> 
      </div>
    </>
  );
}
