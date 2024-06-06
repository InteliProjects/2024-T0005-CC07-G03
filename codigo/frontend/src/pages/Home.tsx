//                                               Resumo da página
// Aqui nós temos a página home, a página principal onde temos alguns serviços, como adicionar saldo, ver quanto de internet já foi utilizado
// E também temos o extrato que ainda não está em funcionamento.
import Saldo from "../components/saldo/Saldo";
import Faturas from "../components/faturas/Faturas";
import Card from "../components/card/CardComponent";
import { useEffect, useState, useRef } from "react";
import axios from "axios";
import Chart, { ChartConfiguration, ChartData } from "chart.js/auto";
import "../../styles.css";
import Img1 from "../assets/img1.png";
import Img2 from "../assets/img2.png";
import Img3 from "../assets/img3.png";

// Interface para armazenar a referência ao gráfico
interface ChartRef {
  chart?: Chart;
}

export default function Home() {
  const [personId, setPersonId] = useState<string | null>(null);
  const [consumoAtual, setConsumoAtual] = useState<number>(0);
  const [consumoTotal, setConsumoTotal] = useState<number>(0);
  const [dataDeAtualizacao, setDataDeAtualizacao] = useState<string | null>(null);

  const chartRef = useRef<HTMLCanvasElement & ChartRef>(null);

  useEffect(() => {
    const id = localStorage.getItem("personId");
    console.log("pagina home: id ", id);
    setPersonId(id);

    if (id == null){
      window.location.href = '/login';
    }
    if (id) {
      // fazendo solicitação
      axios
        .get(`http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/pre_pago/cache/id/${id}`)
        .then((response) => {
          // Atualizando os estados com os dados recebidos
          setConsumoAtual(response.data.consumo_atual);
          setConsumoTotal(response.data.consumo_total);
        })
        .catch((error) => {
          console.error("Erro ao buscar dados da rota:", error);
        });
    }
      axios
        .get(`http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/ultima_atualizacao`)
        .then((response) => {
          setDataDeAtualizacao(response.data.ultima_atualizacao)
        })
        .catch((error) => {
          console.error("Erro ao buscar data de atualização: ", error);
        })
    
  }, [personId]);

  useEffect(() => {
    if (chartRef.current) {
      // Se houver um gráfico anterior, destrua-o
      const existingChart = chartRef.current.chart;
      if (existingChart) {
        existingChart.destroy();
      }

      // Renderize o novo gráfico
      renderChart();
    }
  }, [consumoAtual]);

  // Função para renderizar o gráfico de rosquinha
  const renderChart = () => {
    if (chartRef.current) {
      const ctx = chartRef.current.getContext("2d");
      if (ctx) {
        const chartData: ChartData<"doughnut"> = {
          labels: ["Internet consumida", "Internet Restante"],
          datasets: [
            {
              label: "Internet(GB) ",
              data: [consumoAtual, consumoTotal],
              backgroundColor: ["rgb(120, 0, 157)", "rgb(135, 135, 135)"],
              hoverOffset: 4,
            },
          ],
        };

        const chartConfig: ChartConfiguration<"doughnut"> = {
          type: "doughnut",
          data: chartData,
          options: {
            plugins: {
              legend: {
                display: false,
              },
            },
            layout: {
              padding: {
                bottom: 30,
              },
            },
          },
        };

        const chart = new Chart(ctx, chartConfig);

        // Armazenar o gráfico na referência para posterior destruição
        chartRef.current.chart = chart;
      }
    }
  };

  const pegarTempo = () => {
    let now = new Date();
    return [now.getHours(), now.getMinutes(), now.getSeconds()].map(n => n.toString().padStart(2, '0')).join(':');
  };

  const atualizarDados = () => {
    axios
        .get(`http://backend-load-balancer-1309967107.us-east-1.elb.amazonaws.com/api/prepago/${personId}`)
        .then((response) => {
          setConsumoAtual(response.data.consumo_atual);
          setConsumoTotal(response.data.consumo_total);
          setDataDeAtualizacao(pegarTempo())
        })
        .catch((error) => {
          console.error("Erro ao atualizar dados: ", error);
        })
  }

  return (
    <div className="flex flex-col">
      <div className="flex max-md:flex-col justify-center items-center">
        <div className="w-1/2 -translate-x-40 max-md:-translate-x-0 flex flex-col justify-center items-center">
          {personId && <Saldo id_pessoa={personId} />}
          <Faturas />
        </div>
        <div className="h-96 -translate-x-40 w-[2px] bg-[#78009D] max-md:hidden"></div>
        <div className="home-divider"></div>
        <div className="home-right">
          <p className="home-title">Uso de internet</p>
          <canvas ref={chartRef} className="home-chart"></canvas>
          <p className="home-subtitle">Use como quiser</p>
          <p className="home-subtitle">Já usei {consumoAtual} de {consumoTotal}</p>
          <p className="home-validity">Válido até 20 de Abril</p>
          <p style={{ fontSize: '0.9em', color: 'darkgray' }}>
            Atualizado às {dataDeAtualizacao}
          </p>
          <button onClick={() => atualizarDados()} className="home-button">Atualizar consumo</button>
        </div>
      </div>

      <div className="flex max-md:flex-col items-center justify-center">
        <Card
          img={Img1}
          titulo="6GB por R$33 + cashback todo mês!"
          descricao="No Easy Prime você tem 6GB por R$33, Whatsapp ilimitado e cashback todo mês! Não Falta nada, né?"
          nomebotao="Cadastrar"
          paragrafo="Tem cashback pra você! 🤑"
          id_pessoa={personId ? personId : ""}
          valor={3.3}
          internet={21}

        />
        <Card
          img={Img2}
          titulo="21GB por R$40/mês e cachback!"
          descricao="Confirmado: BÔNUS de internet pra você ficar ainda mais conectado. Com a vivo você pode estar ainda mais perto de quem você ama!"
          nomebotao="Cadastrar"
          paragrafo="Oferta Especial é só aqui no App! ✅"
          id_pessoa={personId ? personId : ""}
          valor={4}
          internet={21}

        />
        <Card
          img={Img3}
          titulo="Bônus de internet para recargas aqui no App 💜"
          descricao="Recarregue a partir de R$17 no PIX ou Cartão de Credito e ganhe bônus! E o melhor: sem gastar sua internet. Aproveite!"
          nomebotao="Registrar"
          paragrafo="Recarregue e Ganhe. 😎"
          id_pessoa={personId ? personId : ""}
          valor={2}
          internet={7}

        />
      </div>
    </div>
  );
}