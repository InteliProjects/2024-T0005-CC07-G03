import { Outlet, useLocation } from "react-router-dom";
import Navbar from "../components/navbar/Navbar";
import Footer from "../components/footer/Footer";

export default function Layout() {
  const location = useLocation();
  const path = location.pathname;
  const isLogin = path === "/login" || path === "/cadastro";
//   const isHome = path === "/";

  return (
    <div className="w-full h-full">
      { !isLogin && <Navbar />}
      <main className="max-h-screen ">
        <Outlet />
      </main>
      { !isLogin && <Footer />}
      
    </div>
  );
}