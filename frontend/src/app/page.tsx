import Image from "next/image";
import { UserImage } from "./components/image";
import { ClickableCard, ClickableCardList } from "./components/clickable_card";
import MaakafLogo from "./components/Layout/logo";

const lowerNavbarItems = [
  {
    href: "https://www.youtube.com/",
    imageSrc: "/stats.png",
    title: "סטטיסטקה",
  },
  {
    href: "https://www.google.com/",
    imageSrc: "/expenses.png",
    title: "הוצאות",
  },
  {
    href: "https://www.google.com/",
    imageSrc: "/tips.png",
    title: "טיפים",
  },
  {
    href: "https://www.google.com/",
    imageSrc: "/savings.png",
    title: "הכנסות",
  },
];

export default function Home() {
  return (
    <main>
      <div className="w-full">
        <div className="z-10 flex size-24 ">
          <MaakafLogo />
        </div>
      </div>

      <h1 className="text-center text-5xl font-bold mb-8 text-white">
        איזה כיף שחזרתה
      </h1>

      <div className="size-2/6 aspect-square">
        <UserImage src="/user.jpg" />
      </div>

      <div className="w-10 h-10"></div>

      <ClickableCardList items={lowerNavbarItems} />
    </main>
  );
}
