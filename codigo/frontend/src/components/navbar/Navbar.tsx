import React, { useState, useEffect } from "react";
import Phone from "../../assets/phone.svg"; // Importação do ícone do telefone
import axios from "axios"; // Importação do axios para fazer requisições HTTP

// Componente de barra de navegação
export default function Navbar() {
  // Estado para armazenar os dados do usuário
  const [userData, setUserData] = useState<any>(null);
  // Estado para controlar a abertura do dropdown
  const [dropdownOpen, setDropdownOpen] = useState<boolean>(false); 

  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState<boolean>(false);

  // Efeito para carregar os dados do usuário ao montar o componente
  useEffect(() => {
    const person_id = localStorage.getItem('personId');

    // Verificar se há um ID de pessoa armazenado no localStorage
    if (person_id) {
      fetchData(person_id); // Buscar os dados do usuário
    }
  }, []);

  // Função para buscar os dados do usuário a partir do ID da pessoa
  const fetchData = async (person_id: string | null) => {
    try {
      if (person_id) {
        // Requisição GET para buscar os dados do usuário pelo ID da pessoa
        const response = await axios.get(`http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa/${person_id}`);
        setUserData(response.data); // Definir os dados do usuário no estado
      }
    } catch (error) {
      console.error("Erro ao buscar os dados:", error);
    }
  };

  // Função para alternar a visibilidade do dropdown
  const handleDropdownToggle = () => {
    setDropdownOpen(!dropdownOpen); 
  };
  
  // Correctly defined handleMobileMenuToggle function
  const handleMobileMenuToggle = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen); // This line toggles the state
  };  


  // Função para realizar o logout do usuário
  const handleLogout = () => {
    localStorage.clear(); // Limpar os dados do localStorage
    window.location.href = "/login"; // Redirecionar para a página de login
  };

  return (
      <nav className="w-full h-24 bg-[#78009D] flex items-center justify-center relative">
        <div className="w-4/5 flex items-center justify-between max-md:hidden">
          <h1 className="text-white text-[40px]">Meu Plano</h1>
        </div>
        {/* Renderizar o nome do usuário e o dropdown de opções */}
        {userData && (
          <div className="relative max-md:mb-8">
            <p className="text-white text-[20px] font-bold cursor-pointer" onClick={handleDropdownToggle}>
              {userData.nome}
            </p>
            {/* Dropdown com a opção de sair */}
            {dropdownOpen && (
              <div className="absolute top-full right-0 mt-2 bg-white p-2 rounded shadow">
                <button onClick={handleLogout} className="block w-full text-left text-gray-800 hover:bg-gray-200 px-4 py-2">
                  Sair
                </button>
              </div>
            )}
          </div>
        )}
        {/* Renderizar os dados do plano do usuário */}
        {userData && (
          <div className="flex items-center w-96 h-20 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y bg-white p-8 shadow-lg rounded-lg">
            <img src={Phone} alt="Ícone do telefone" className="w-8 h-8 ml-1" />
            <div className="ml-4">
              <p className="font-bold text-[20px]">{userData.tipo === 'pre' ? 'Pré-Pago' : 'Pós-Pago'}</p>
              <p className="text-[#757575] text-[20px]">{userData.numero}</p>
            </div>
          </div>
        )}
      </nav>
    );
  }
