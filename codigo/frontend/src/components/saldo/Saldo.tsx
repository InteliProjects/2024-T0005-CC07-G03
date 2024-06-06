import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Seta from "../../assets/seta.svg";
import axios from "axios";

export default function Saldo({ id_pessoa }: { id_pessoa: string }) {
  // Estado para armazenar o saldo do usuário
  const [saldo, setSaldo] = useState<number | null>(null);
  // Estado para armazenar a resposta da requisição de dados do usuário
  const [userDataResponse, setUserDataResponse] = useState<any>(null);

  // Efeito para buscar os dados do usuário e o saldo ao montar o componente ou quando o ID da pessoa muda
  useEffect(() => {
    fetchData();
  }, [id_pessoa]);

  // Função para buscar os dados do usuário e o saldo
  const fetchData = async () => {
    try {
      // Requisição GET para buscar os dados do usuário pelo ID da pessoa
      const response = await axios.get(
        `http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa/${id_pessoa}`
      );
      setUserDataResponse(response.data); // Definir os dados do usuário na resposta

      // Verificar se o usuário possui um ID de pré-pago
      if (response.data.id_pre !== undefined) {
        // Requisição GET para buscar o saldo do usuário pré-pago pelo ID do usuário
        const saldoResponse = await axios.get(
          `http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/prepago/${response.data.id_pre}`
        );
        const saldoValue = saldoResponse.data.saldo; // Extrair o saldo da resposta
        setSaldo(saldoValue); // Definir o saldo no estado
      }
    } catch (error) {
      console.error("Erro ao buscar os dados:", error);
    }
  };

  // Função para adicionar saldo ao usuário pré-pago
  const adicionarSaldo = async () => {
    try {
      // Verificar se há uma resposta de dados do usuário e se ele possui um ID de pré-pago
      if (userDataResponse !== null && userDataResponse.id_pre !== undefined) {
        // Requisição PUT para adicionar saldo ao usuário pré-pago
        const response = await axios.put(
          `http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/prepago/adicionar_saldo/${userDataResponse.id_pre}`,
          {
            valor_adicionado: 15, // Valor a ser adicionado ao saldo
          }
        );
        console.log(response); // Log da resposta
        fetchData(); // Atualizar os dados do usuário e o saldo após a adição do saldo
      }
    } catch (error) {
      console.error("Erro ao adicionar saldo:", error);
    }
  };

  return (
    <>
      {/* Componente de saldo */}
      <div className="flex flex-col h-48 w-[370px] max-md:w-[340px] border border-[#D3D3D3] pt-[20px] rounded-[8px] mt-10">
        <div className="flex flex-col items-start pl-4">
          {/* Título do saldo */}
          <div className="flex text-center justify-center w-40 bg-[#ECF8E7] rounded-[20px] border border-[#0B5112] mb-4">
            <p className="text-[#557961] font-bold">Saldo Disponível</p>
          </div>
          {/* Informações do saldo */}
          <p className="text-[#757575]">Válido até 02 de março de 2024</p>
          <p className="text-[26px] font-bold">
            {saldo !== null ? saldo : "Sem saldo"}
          </p>
        </div>
        <div className="flex items-center pl-10 pt-[10px]">
          {/* Botão para adicionar saldo */}
          <button
            onClick={() => {
                adicionarSaldo();
                console.log("Adicionando saldo")
            }}
            className={`h-10 w-36 bg-[#8016a0] hover:bg-purple-700 text-white font-bold flex items-center justify-center rounded-[4px]`}
          >
            Fazer Recarga
          </button>
          {/* Link para ver o extrato */}
          <Link
            to={"teste"}
            className="flex items-center ml-10 text-[#78009D] font-bold"
          >
            <p>Ver Extrato</p>
            <img src={Seta} alt="Seta" className="w-4 h-4 ml-1 bg-[#]" />
          </Link>
        </div>
      </div>
    </>
  );
}