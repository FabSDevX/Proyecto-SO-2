import "./Stats.css";
import { useEffect, useState } from "react";
// import { BarChart } from "@mui/x-charts/BarChart";
// import { PieChart } from "@mui/x-charts/PieChart";
import { BarLoader } from "react-spinners";


export function Stats(){
  const [isLoading, setIsLoading] = useState(true);
  // const [chartResult, setChartResult] = useState<{
  //   categories: string[];
  //   confidence: number[];
  // }>({ categories: [], confidence: [] });
  useEffect(() => {
    const start = Date.now();
    setIsLoading(true);
    console.log("Starting analysis...");
  }, []);

  
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
        <p>ss</p>
          {/* <div className="stats-section">
            <div className="container">
              <div className="stats-container">
                {chartResult.categories.length > 0 &&
                chartResult.confidence.length > 0 ? (
                  selectedGraphOption === "Barras" ? (
                    <BarChart className="barchar"
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
                    No hay datos disponibles para mostrar para{" "}
                    {selectedAnalysisOption}.
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
          </div> */}
        </>
      )}
    </section>
  );
};
