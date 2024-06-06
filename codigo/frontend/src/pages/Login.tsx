import React from "react";
import LoginComponent from "../components/loginComponent/LoginComponent";
import img_vivocadastro from "../assets/img_vivo4.png";
import "../../styles.css"; // Importando o arquivo de estilos global

export default function Login() {
  return (
    <div className="flex flex-col md:flex-row h-screen w-full">
      <div className="w-full md:w-1/2 relative">
        {/* Aqui você mantém a proporção da imagem */}
        <div
          className="bg-cover bg-center"
          style={{
            paddingTop: "56.25%" // 16:9 aspect ratio
          }}
        >
          {/* Dentro da div da imagem */}
          <img
            className="absolute inset-0 w-full h-full object-cover max-w-full max-h-full"
            src={img_vivocadastro}
            alt="Imagem"
          />
        </div>
      </div>

      <div className="w-full md:w-1/2 flex flex-col justify-center items-center p-8 md:p-0">
        <h1 className="text-3xl md:text-4xl font-bold mb-4 md:mb-0 md:translate-y-20" >Login</h1>
        <p className="text-lg md:text-xl mb md:mb-8 md:translate-y-20">Preencha os campos abaixo para logar na sua conta</p>
        <LoginComponent />
      </div>
    </div>
  );
}
