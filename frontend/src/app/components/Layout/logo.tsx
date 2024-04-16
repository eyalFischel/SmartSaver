/* eslint-disable @next/next/no-img-element */
import React from "react";

interface CustomLinkProps {
  href: string;
  src: string;
}

const CustomLogo: React.FC<CustomLinkProps> = ({ href, src }) => {
  return (
    <a
      className=" flex place-items-center gap-4 p-4 size-fit"
      href={href}
      target="_blank"
      rel="noopener noreferrer"
    >
      <img className="size-fit" src={src} alt="Logo" />
    </a>
  );
};

// Specific instance of CustomLink component with maakaf logo and maakaf link
const MaakafLogo: React.FC = () => {
  return (
    <CustomLogo
      href="https://maakaf-landing-page.netlify.app"
      src="/maakaf.png"
    />
  );
};

export default MaakafLogo;
