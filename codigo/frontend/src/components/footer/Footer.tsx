import Vivo from '../../assets/vivo.svg';

export default function Footer() {
  return (
    <div className="py-6 px-4 fixed bottom-0 right-0 max-md:hidden">
      <div className="container mx-auto flex justify-end">
        <img src={Vivo} alt="Logo da Vivo" className="w-36 h-auto" />
      </div>
    </div>
  );
}
