import React from "react";
import Link from "next/link";

interface ClickableCardProps {
  href: string;
  imageSrc: string;
  title: string;
}

interface ClickableCardListProps {
  items: ClickableCardProps[];
}

const ClickableCard: React.FC<ClickableCardProps> = ({
  href,
  imageSrc,
  title,
}) => {
  return (
    <Link
      href={href}
      className=" inline-block bg-white rounded-lg shadow-gray  p-4 mb-4  text-center "
    >
      <h3 className="text-lg font-semibold text-black">{title}</h3>
      <img src={imageSrc} alt={title} className="w-auto h-auto " />
    </Link>
  );
};

const ClickableCardList: React.FC<ClickableCardListProps> = ({ items }) => {
  return (
    <div className="grid grid-cols-auto-fill grid-flow-col gap-4 justify-center w-full ">
      <div className="h-5%"></div>
      {items.map((item, index) => (
        <ClickableCard
          key={index}
          href={item.href}
          imageSrc={item.imageSrc}
          title={item.title}
        />
      ))}
      <div className="h-5%"></div>
    </div>
  );
};

export { ClickableCard, ClickableCardList };
