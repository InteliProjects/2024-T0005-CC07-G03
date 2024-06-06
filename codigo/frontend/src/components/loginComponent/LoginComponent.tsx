import * as Tabs from "@radix-ui/react-tabs";
import React, { useState } from "react";
import InputMask from "react-input-mask";
import { Link } from "react-router-dom";

// Componente de login
export default function LoginComponent() {
  // Definindo estados para os campos do formulário
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [id_pessoa, setPersonId] = useState<string | null>(null);
  const [phoneNumber, setPhoneNumber] = useState("");

  // Função para lidar com mudanças no campo de CPF ou E-mail
  const handleCpfOrEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setEmail(value);
  };

  // Função para lidar com mudanças no campo de número de telefone
  const handlePhoneNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setPhoneNumber(value);
  };

  // Função para lidar com mudanças no campo de senha
  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setPassword(value);

    // Verificar se a senha é válida
    const hasUppercase = /[A-Z]/.test(value);
    const hasNumber = /\d/.test(value);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(value);
    const isValidPassword = hasUppercase && hasNumber && hasSpecialChar;

    // Definir mensagem de erro se a senha não for válida
    if (!isValidPassword) {
      setErrorMessage(
        "A senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial."
      );
    } else {
      setErrorMessage("");
    }
  };

    // Função para lidar com o login
    const handleLogin = async () => {
        let response: Response | null = null;
        try {
            // Definir a URL da rota de autenticação com base na aba selecionada (número Vivo ou email)
            let authURL;
            if (email) {
                authURL = `http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa/autenticar_email/${email}`;
            } else if (phoneNumber) {
                authURL = `http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa/autenticar_numero/${phoneNumber}`;
            } else {
                throw new Error('Nenhum email ou número de telefone fornecido.');
            }
    
            // Realizar a requisição para a rota de autenticação
            response = await fetch(authURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ senha: password }), // Enviar a senha no corpo da requisição
            });
    
            // Verificar se a autenticação foi bem-sucedida
            if (response.status === 201) {
                const data = await response.json();
                if (data === true) {
                    // Autenticação bem-sucedida, realizar outras operações necessárias
                    console.log('Autenticação bem-sucedida!');
                    // Verificar se o usuário é autenticado antes de buscar informações
                    if (data === true) {
                        if (email) {
                            response = await fetch(`http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa/email/${email}`);
                        } else if (phoneNumber) {
                            response = await fetch(`http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa/numero/${phoneNumber}`);
                        }
                        // Tratar a resposta da requisição
                        if (response && response.ok) {
                            const data = await response.json();
                            const personId = data.id_pessoa;
                            setPersonId(personId);
                            console.log('ID da pessoa:', personId);
                            localStorage.setItem('personId', personId);
                        } // Atualizar os dados do usuário após o login
                        window.location.href = '/';
                        console.log("cheguei aqui")
                    }
                } else {
                    // Autenticação falhou, mostrar mensagem de erro
                    console.log('Autenticação falhou.');
                    // Aqui você pode definir um estado para mostrar uma mensagem de erro no frontend
                }
            } else if (response.status === 401) {
                // Autenticação falhou com status 401 (Unauthorized)
                console.log('Autenticação falhou: Não autorizado');
                // Aqui você pode definir um estado para mostrar uma mensagem de erro no frontend
            } else {
                throw new Error('Erro ao autenticar.');
            }
        } catch (error) {
            console.error('Erro ao realizar login:', error);
            // Tratar erros de requisição, como falha na conexão ou erro no servidor
            // Aqui você pode definir um estado para mostrar uma mensagem de erro no frontend
        }
    };

  return (
    <Tabs.Root defaultValue="tab1" className="login-component-root">
      <Tabs.List aria-label="Options for login" className="login-tabs-list">
        <Tabs.Trigger value="tab1" className="login-tab">
          Número Vivo
        </Tabs.Trigger>
        <Tabs.Trigger value="tab2" className="login-tab">
          Email
        </Tabs.Trigger>
      </Tabs.List>
      {/* Conteúdo das abas */}
      <Tabs.Content
        className="grow p-5 bg-white rounded-b-md outline-none"
        value="tab1"
      >
        {/* Conteúdo do login com número Vivo */}
        <p className="mb-5 text-mauve11 text-[15px] leading-normal">
          Faça login com seu número de telefone
        </p>
        {/* Formulário de login com número de telefone */}
        <fieldset className="mb-[15px] w-full flex flex-col justify-start">
          <label
            className="text-[13px] leading-none mb-2.5 text-violet12 block"
            htmlFor="phoneNumber"
          >
            Número
          </label>
          <InputMask
            mask="(99)99999-9999"
            maskChar=""
            placeholder="(99)99999-9999"
            className="w-full h-[45px] px-4 py-2 mb-2 border border-gray-300 rounded-md"
            value={phoneNumber}
            onChange={handlePhoneNumberChange}
          />
        </fieldset>
        {/* Campo de senha */}
        <fieldset className=" w-full flex flex-col justify-start">
          <label
            className="text-[13px] leading-none mb-2.5 text-violet12 block"
            htmlFor="password"
          >
            Password
          </label>
          <input
            className="w-full h-[45px] px-4 py-2 mb-2 border border-gray-300 rounded-md"
            id="password"
            placeholder="**********"
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
          {errorMessage && <p className="text-red-500">{errorMessage}</p>}
        </fieldset>
        <Link to="/cadastro" className="text-blue-700">
          {" "}
          Esqueceu a senha?
        </Link>
        {/* Botão de login */}
        <div className="flex flex-col justify-end mt-5">
          <button
            className="inline-flex items-center justify-center mt-2 bg-black rounded px-4 md:px-[15px] text-base md:text-[15px] leading-none font-medium h-[45px] w-full md:w-auto max-w-[360px] md:max-w-none bg-[#8016a0] hover:bg-purple-700 focus:shadow-[0_0_0_2px] focus:shadow-green7 text-white outline-none cursor-pointer"
            onClick={handleLogin}
          >
            Entrar
          </button>
          <p>
            Ainda não tem uma conta?{" "}
            <Link to="/cadastro" className="text-blue-700">
              Clique aqui.
            </Link>
          </p>
        </div>
      </Tabs.Content>
      {/* Conteúdo da aba de login com E-mail */}
      <Tabs.Content
        className="grow p-5 bg-white rounded-b-md outline-none focus:shadow-[0_0_0_2px] focus:shadow-black"
        value="tab2"
      >
        <p className="mb-5 text-mauve11 text-[15px] leading-normal">
          Faça login com E-mail
        </p>
        {/* Formulário de login com E-mail */}
        <fieldset className="mb-[15px] w-full flex flex-col justify-start">
          <label
            className="text-[13px] leading-none mb-2.5 text-violet12 block"
            htmlFor="currentPassword"
          >
            E-mail
          </label>
          <input
            className="w-full h-[45px] px-4 py-2 mb-2 border border-gray-300 rounded-md"
            placeholder="johndoe@gmail.com"
            type="text"
            value={email}
            onChange={handleCpfOrEmailChange}
          />
        </fieldset>
        {/* Campo de senha */}
        <fieldset className=" w-full flex flex-col justify-start">
          <label
            className="text-[13px] leading-none mb-2.5 text-violet12 block"
            htmlFor="password"
          >
            Password
          </label>
          <input
            className="w-full h-[45px] px-4 py-2 mb-2 border border-gray-300 rounded-md"
            id="password"
            placeholder="**********"
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
          {errorMessage && <p className="text-red-500">{errorMessage}</p>}
        </fieldset>
        <Link to="/cadastro" className="text-blue-700">
          {" "}
          Esqueceu a senha?
        </Link>
        {/* Botão de login */}
        <div className="flex  flex-col justify-end mt-5">
          <button
            type="submit"
            className="inline-flex items-center justify-center mt-2 bg-black rounded px-4 md:px-[15px] text-base md:text-[15px] leading-none font-medium h-[45px] w-full md:w-auto max-w-[360px] md:max-w-none bg-[#8016a0] hover:bg-purple-700 focus:shadow-[0_0_0_2px] focus:shadow-green7 text-white outline-none cursor-pointer"
            
            onClick={handleLogin}
          >
            Entrar
          </button>
          <p>
            Ainda não tem uma conta?{" "}
            <Link to="/cadastro" className="text-blue-700">
              Clique aqui.
            </Link>
          </p>
        </div>
      </Tabs.Content>
    </Tabs.Root>
  );
}
