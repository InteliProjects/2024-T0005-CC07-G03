import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea, CardActions, Modal, Button } from '@mui/material';
import axios from 'axios';
import { useEffect, useState } from 'react';

export default function CardComponent({ img, paragrafo, titulo, descricao, nomebotao, id_pessoa, valor, internet }: { img: string, paragrafo: string,titulo: string, descricao: string, nomebotao: string, id_pessoa: string, valor: number, internet: number}) {
  const [open, setOpen] = React.useState(false); // Estado para controlar a abertura e fechamento do modal
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
            valor_adicionado: valor, // Valor a ser adicionado ao saldo
          }
        );
        console.log(response); // Log da resposta
        fetchData(); // Atualizar os dados do usuário e o saldo após a adição do saldo
      }
    } catch (error) {
      console.error("Erro ao adicionar saldo:", error);
    }
  };
  const adicionarNet = async () => {
    try {
      // Verificar se há uma resposta de dados do usuário e se ele possui um ID de pré-pago
      if (userDataResponse !== null && userDataResponse.id_pre !== undefined) {
        // Requisição PUT para adicionar saldo ao usuário pré-pago
        const response = await axios.put(
          `http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/prepago/adicionar_consumo_total/${userDataResponse.id_pre}`,
          {
            valor_adicionado: internet, // Valor a ser adicionado ao saldo
          }
        );
        console.log(response); // Log da resposta
        fetchData(); // Atualizar os dados do usuário e o saldo após a adição do saldo
      }
    } catch (error) {
      console.error("Erro ao adicionar saldo:", error);
    }
  };
  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleAcceptOffer = () => {
    adicionarSaldo();
    adicionarNet();
    handleClose(); // Fecha o modal após aceitar a oferta
  };

  return (
    <>
    <Card sx={{ maxWidth: 345 }} className='pr-4 mt-10 max-md:ml-0 mb-4'>
  <CardActionArea>
    <CardMedia
      component="img"
      height="140"
      image={img}
      alt="green iguana"
    />
    <p className='pt-4 pl-4'>{paragrafo}</p>
    <CardContent>
      <Typography gutterBottom variant="h5" component="div">
        {titulo}
      </Typography>
      <Typography variant="body2" color="text.secondary">
        {descricao}
      </Typography>
    </CardContent>
  </CardActionArea>
  <CardActions>
    <Button
      className={`mt-4 ml-2 h-10 w-32 bg-[#8016a0] hover:bg-purple-700 text-white font-bold flex items-center justify-center rounded-[4px]`}
      onClick={handleOpen}
    >
      {nomebotao}
    </Button>
  </CardActions>
</Card>

{/* Modal para aceitar oferta */}
<Modal
  open={open}
  onClose={handleClose}
  aria-labelledby="modal-modal-title"
  aria-describedby="modal-modal-description"
>
  <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-4 rounded" style={{ width: '80%', height: '60%', maxWidth: '400px', maxHeight: '150px'}}>
    <Typography id="modal-modal-title" variant="h6" component="h2" align="center">
      Aceitar Oferta?
    </Typography>
    <div className="flex justify-center mt-4">
      <Button variant="contained" onClick={handleAcceptOffer} sx={{ bgcolor: 'green', mr: 2 }}>
        Sim
      </Button>
      <Button variant="contained" onClick={handleClose}>
        Não
      </Button>
    </div>
  </div>
</Modal>

    </>
  );
}
