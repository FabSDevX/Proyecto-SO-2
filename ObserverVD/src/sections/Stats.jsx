import { useEffect, useState } from "react";
import { BarChart } from "@mui/x-charts/BarChart";
import { PieChart } from "@mui/x-charts/PieChart";
import { BarLoader } from "react-spinners";
import { processVideo } from "../utils/apis/postApi";
import "./Stats.css";
import propTypes from "prop-types";

export function Stats({ selectedVideo, selectedActor }) {
  const [isLoading, setIsLoading] = useState(true);
  const [chartResult, setChartResult] = useState({
    categories: [],
    confidence: [],
  });
  const [selectedGraphOption, setSelectedGraphOption] = useState("Barras");
  useEffect(() => {
    setIsLoading(true);
    handleData();
    console.log("Starting analysis...");
  }, []);

  const handleNavGraphOption = async (identifier) => {
    setSelectedGraphOption(identifier);
  };

  async function handleData() {
    const response = await processVideo(selectedActor,selectedVideo)
    if (response != null) {
      // Extraer las categorías y las confidencias del objeto de respuesta.
      const categories = Object.keys(response);
      const confidence = Object.values(response);

      // Actualizar el estado con los nuevos valores.
      setChartResult({
        categories,
        confidence,
      });
      setIsLoading(false);
    } else {
      alert("Error en la respuesta");
    }
  }

  return (
    <section>
      {isLoading ? (
        <>
          <div className="loading-section">
            <p>Procesando datos</p>
            <BarLoader width={200} height={5} color="#36d7b7" />
            <img
              src="https://media1.tenor.com/m/Ge1njBV_AQkAAAAC/waiting-im-waiting.gif"
              alt="Waiting gif"
            />
          </div>
        </>
      ) : (
        <>
          <div className="stats-section">
            <div className="container">
              <div className="stats-container">
                {chartResult.categories.length > 0 &&
                chartResult.confidence.length > 0 ? (
                  selectedGraphOption === "Barras" ? (
                    <BarChart
                      className="barchar"
                      xAxis={[
                        {
                          id: "barCategories",
                          data: chartResult.categories,
                          scaleType: "band",
                        },
                      ]}
                      series={[
                        {
                          data: chartResult.confidence,
                        },
                      ]}
                      width={500}
                      height={500}
                    />
                  ) : (
                    <PieChart
                      series={[
                        {
                          data: chartResult.confidence.map((value, index) => ({
                            id: index,
                            value: value,
                            label: chartResult.categories[index],
                          })),
                        },
                      ]}
                      width={400}
                      height={400}
                    />
                  )
                ) : (
                  <p className="stats-paragraph">
                    No hay datos disponibles para mostrar para
                  </p>
                )}
              </div>
              <ul className="lateral-right-navigation">
                <li>
                  <a
                    className={
                      selectedGraphOption === "Barras" ? "selectedGraph" : ""
                    }
                    onClick={() => handleNavGraphOption("Barras")}
                  >
                    Barras
                  </a>
                </li>
                <li>
                  <a
                    className={
                      selectedGraphOption === "Pastel" ? "selectedGraph" : ""
                    }
                    onClick={() => handleNavGraphOption("Pastel")}
                  >
                    Pastel
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </>
      )}
    </section>
  );
}

Stats.propTypes = {
  selectedActor: propTypes.any,
  selectedVideo: propTypes.any,
};
