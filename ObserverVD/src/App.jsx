import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { LandPage } from "./pages/LandPage";
import { Reports } from "./pages/Reports";
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandPage />} />
        <Route path="/reports" element={<Reports />} />
      </Routes>
    </Router>
  );
}

export default App;
