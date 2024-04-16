/* eslint-disable @next/next/no-img-element */
import React from "react";

interface UserImageProps {
  src: string;
}

const UserImage: React.FC<UserImageProps> = ({ src }) => {
  return (
    <img
      alt="alt text"
      src={src}
      className="flex rounded-full outline border-3 border-black h-full w-full "
    />
  );
};

export { UserImage };
