// este é um componente de fatura, onde nós escolhemos o mês e pegamos a fatura do mês em que escolhemos
import FormControl from '@mui/material/FormControl';
import { NativeSelect } from "@mui/material";

export default function Faturas(){
    return (
        <>
            <div className="flex flex-col h-48 w-[370px] max-md:w-[340px] border border-[#D3D3D3] pt-[10px] mt-10 rounded-[8px] mb-6">
                <p className="text-[#78009D] text-[26px] font-bold self-center">Emitir Faturas</p>
                <div className="flex flex-col items-start pl-10">
                    <div className="flex text-center justify-center w-40 bg-[#ECF8E7] rounded-[20px] border border-[#0B5112] mb-2 mt-2">
                        <p className="text-[#557961] font-bold">Faturas Disponíveis</p>
                    </div>
                    <div className="flex items-center">
                        <label className="text-[18px] mr-4 font-bold">Mês:</label>
                        {/* iniciando forms para pegar dados e jogar para o extrato */}
                        <FormControl >
                            <NativeSelect
                                inputProps={{
                                id: 'uncontrolled-native',
                                }}
                            >
                                <option value="jan">Janeiro</option>
                                <option value="feb">Fevereiro</option>
                                <option value="mar">Março</option>
                                <option value="apr">Abril</option>
                                <option value="may">Maio</option>
                                <option value="jun">Junho</option>
                                <option value="jul">Julho</option>
                                <option value="aug">Agosto</option>
                                <option value="sep">Setembro</option>
                                <option value="oct">Outubro</option>
                                <option value="nov">Novembro</option>
                                <option value="dec">Dezembro</option>
                            </NativeSelect>
                        </FormControl>
                    </div>
                </div>
                <div className="flex items-center pl-10 pt-[10px]">
                    <button className="h-10 w-36 bg-[#8016a0] hover:bg-purple-700 text-white font-bold flex items-center justify-center rounded-[4px]">Emitir Fatura</button>
                </div>
            </div>
        </>
    )
}