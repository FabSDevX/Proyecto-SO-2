import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";
import "./AvatarCards.css";
import messi from "../assets/webp/messi.webp";
import john from "../assets/webp/johnKrasinski.webp";
import propTypes from "prop-types";
import { useState } from "react";

export function AvatarCards({ handleActorData }) {
  const [selectedActor, setSelectedActor] = useState(null);

  const handleClick = (actor) => {
    const newSelectedActor = selectedActor === actor ? null : actor;
    setSelectedActor(newSelectedActor);
    handleActorData(newSelectedActor);
  };
  return (
    <section className="avatarCards">
      <div className="cards">
        <Card onClick={() => handleClick("leonelMessi")}  className={`card-left cardsAvatar ${selectedActor === "leonelMessi" ? "selected" : ""}`} sx={{ maxWidth: 345 }}>
          <CardActionArea>
            <CardMedia
              component="img"
              height="500px"
              image={messi}
              alt="Leonel messi"
            />
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                Leonel Messi
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Conocido como Leo o Pulga, su inmensa calidad ya apuntaba cuando
                tenía cinco años y jugaba en el club de barrio de su ciudad
                natal dirigido por su padre, un empleado de la industria
                metalúrgica, y se reafirmó cuando, a partir de sus siete años.
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card >
        <Card onClick={() => handleClick("johnKrasinski")}  className={`card-right cardsAvatar ${selectedActor === "johnKrasinski" ? "selected" : ""}`} sx={{ maxWidth: 345 }}>
          <CardActionArea>
            <CardMedia
              component="img"
              height="500px"
              image={john}
              alt="John Krasinski"
            />
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                John Krasinski
              </Typography>
              <Typography variant="body2" color="text.secondary">
                John Krasinski es un actor y cineasta estadounidense conocido
                principalmente por su papel como Jim Halpert en la serie de NBC
                “The Office” (2005-2013), donde también fue productor y director
                ocasional.
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
      </div>
    </section>
  );
}

AvatarCards.propTypes = {
  handleActorData: propTypes.any.isRequired,
};


