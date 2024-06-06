import * as Label from "@radix-ui/react-label";
import { FormEvent, useState } from "react";
import InputMask from "react-input-mask";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

// Função para validar CPF.
function validarCPF(cpf: any) {
  cpf = cpf.replace(/[^\d]+/g, "");
  if (cpf === "") return false;
  if (
    cpf.length !== 11 ||
    cpf === "00000000000" ||
    cpf === "11111111111" ||
    cpf === "22222222222" ||
    cpf === "33333333333" ||
    cpf === "44444444444" ||
    cpf === "55555555555" ||
    cpf === "66666666666" ||
    cpf === "77777777777" ||
    cpf === "88888888888" ||
    cpf === "99999999999"
  )
    return false;
  let add = 0;
  for (let i = 0; i < 9; i++) add += parseInt(cpf.charAt(i)) * (10 - i);
  let rev = 11 - (add % 11);
  if (rev === 10 || rev === 11) rev = 0;
  if (rev !== parseInt(cpf.charAt(9))) return false;
  add = 0;
  for (let i = 0; i < 10; i++) add += parseInt(cpf.charAt(i)) * (11 - i);
  rev = 11 - (add % 11);
  if (rev === 10 || rev === 11) rev = 0;
  if (rev !== parseInt(cpf.charAt(10))) return false;
  return true;
}

// Componente de cadastro.
export default function CadastroComponent() {
  // Definindo estados para os campos do formulário.
  const [nome, setNome] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [cpf, setCpf] = useState<string>("");
  const [numero, setNumero] = useState<string>("");
  const [senha, setSenha] = useState<string>("");
  const [nomeValido, setNomeValido] = useState<boolean>(true);
  const [senhaValida, setSenhaValida] = useState<boolean>(true);
  const [emailValido, setEmailValido] = useState<boolean>(true);
  const [cpfValido, setCpfValido] = useState<boolean>(true);
  const [numeroValido, setNumeroValido] = useState<boolean>(true);
  const [errorMessage, setErrorMessage] = useState<string>("");

  // Função para lidar com o envio do formulário.
  const handleSubmit = async (e: FormEvent<HTMLFormElement>): Promise<void> => {
    // Prevenir comportamento padrão do formulário.
    e.preventDefault();

    // Verificar se os campos obrigatórios estão preenchidos.
    if (!nome || !email || !cpf || !numero) {
      if (!nome) setNomeValido(false);
      if (!email) setEmailValido(false);
      if (!cpf) setCpfValido(false);
      if (!numero) setNumeroValido(false);
      return;
    }

    // Validar o CPF inserido.
    if (!validarCPF(cpf)) {
      setCpfValido(false);
      return;
    }

    // Construir objeto de dados a serem enviados.
    const data = {
      nome: nome,
      email: email,
      cpf: cpf,
      numero: numero,
      tipo: "pre",
      senha: senha,
    };

        try {
            // Enviar os dados para o servidor.
            const response = await fetch('http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pessoa', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            // Tratar resposta do servidor.
            if (!response.ok) {
                toast.error('Erro ao cadastrar pessoa');
            }

      console.log("Pessoa cadastrada com sucesso!");
      toast.success("Cadastro Efetuado com sucesso");
      window.location.href = '/login';

    } catch (error) {
      // Lidar com erros de requisição.
      if (error instanceof Error) {
        setErrorMessage(error.message);
      }
    }
  };

  return (
    <div className="formulario-cad">
      <form onSubmit={handleSubmit}>
        {/* Campo de nome */}
        <div className="flex flex-col mb-4">
          <Label.Root htmlFor="nome" className="text-[15px] font-medium mb-1">
            Nome Completo
          </Label.Root>
          <input
            className={`input-field ${
              !nomeValido && "border-red"
            } border-2 border-black rounded-md w-full py-2 px-3`}
            type="text"
            id="nome"
            placeholder="John"
            value={nome}
            onChange={(e) => {
              setNome(e.target.value);
              setNomeValido(true);
            }}
          />
          {!nomeValido && <p className="text-[#DA0E0E]">Campo obrigatório</p>}
        </div>
        {/* Campo de email */}
        <div className="flex flex-col mb-4">
          <Label.Root htmlFor="email" className="text-[15px] font-medium mb-1">
            Email
          </Label.Root>
          <input
            className={`input-field ${
              !emailValido && "border-red"
            } border-2 border-black rounded-md w-full py-2 px-3`}
            type="text"
            id="email"
            placeholder="johndoe@gmail.com"
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
              setEmailValido(true);
            }}
          />
          {!emailValido && <p className="text-[#DA0E0E]">Campo obrigatório</p>}
        </div>
        {/* Campos de CPF e número, utilizando máscaras de entrada */}
        <div className="flex mb-4">
          <div className="flex flex-col mr-4 w-1/2">
            <Label.Root htmlFor="cpf" className="text-[15px] font-medium mb-1">
              CPF
            </Label.Root>
            <InputMask
              className={`input-field ${
                !cpfValido && "border-red"
              } border-2 border-black rounded-md w-full py-2 px-3`}
              mask="999.999.999-99"
              type="text"
              id="cpf"
              placeholder="999.999.999-99"
              value={cpf}
              onChange={(e) => {
                setCpf(e.target.value);
                setCpfValido(true);
              }}
            />
            {!cpfValido && <p className="text-[#DA0E0E]">CPF inválido</p>}
          </div>
          <div className="flex flex-col w-1/2">
            <Label.Root
              htmlFor="numero"
              className="text-[15px] font-medium mb-1"
            >
              Número
            </Label.Root>
            <InputMask
              className={`input-field ${
                !numeroValido && "border-red"
              } border-2 border-black rounded-md w-full py-2 px-3`}
              mask="(99)99999-9999"
              placeholder="(99)99999-9999"
              type="text"
              id="numero"
              value={numero}
              onChange={(e) => {
                setNumero(e.target.value);
                setNumeroValido(true);
              }}
            />
            {!numeroValido && (
              <p className="text-[#DA0E0E]">Campo obrigatório</p>
            )}
          </div>
        </div>
        {/* Campo de senha */}
        <div className="flex flex-col mb-4">
          <Label.Root htmlFor="senha" className="text-[15px] font-medium mb-1">
            Senha
          </Label.Root>
          <input
            className={`input-field ${
              !senhaValida && "border-red"
            } border-2 border-black rounded-md w-full py-2 px-3`}
            type="password"
            id="senha"
            placeholder="*********"
            value={senha}
            onChange={(e) => {
              setSenha(e.target.value);
              setSenhaValida(true);
            }}
          />
          {!senhaValida && <p className="text-[#DA0E0E]">Campo obrigatório</p>}
        </div>
        {/* Botão de submit */}
        <button
          type="submit"
          className="inline-flex items-center justify-center mt-10 bg-black rounded px-4 py-2 text-[15px] leading-none font-medium max-md:h-[45px] w-full md:max-w-full bg-green4 text-green11 hover:bg-green5 hover:bg-purple-600 focus:shadow-[0_0_0_2px] focus:shadow-green7 text-white outline-none cursor-pointer"
        >
          Cadastrar
        </button>

        {/* Container para exibição de notificações */}
        <ToastContainer
          position="top-right"
          autoClose={2000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick={true}
          rtl={false}
          className={"text-center"}
          pauseOnFocusLoss={false}
          draggable={true}
          pauseOnHover={true}
          theme="light"
        />
      </form>
    </div>
  );
}
