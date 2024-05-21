import PropTypes from "prop-types";
import "./Hero.css";

export function Hero(props) {
  const { title, paragraph, image } = props;

  return (
    <section className="hero-container">
      <div className="hero-left">
        <h1>{title}</h1>
        <p>{paragraph}</p>
      </div>
      <div className="hero-right">
        <img src={image} alt="Detection video image" />
      </div>
    </section>
  );
}

Hero.propTypes = {
  title: PropTypes.string.isRequired,
  paragraph: PropTypes.string.isRequired,
  image: PropTypes.string.isRequired,
};
