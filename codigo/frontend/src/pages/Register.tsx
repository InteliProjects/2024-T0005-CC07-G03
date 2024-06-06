import React from 'react';
import CadastroComponent from "../components/cadastroComponent/CadastroComponent";
import Vivo from '../assets/vivo.svg';
import img_vivocadastro from '../assets/img_vivo4.png';

export default function Register() {
  return (
    <div className="register-container">
      <div className="register-background" style={{backgroundImage: `url(${img_vivocadastro})`}}>
        {/* Background image is set via CSS for better responsiveness */}
      </div>
      <div className="register-form">
        <h1 className="register-title">Cadastro</h1>
        <p className="register-description">Preencha os campos abaixo para fazer seu cadastro</p>
        <CadastroComponent />
        <img src={Vivo} alt="Logo da Vivo" className="vivo-logo" />
      </div>
    </div>
  );
}
