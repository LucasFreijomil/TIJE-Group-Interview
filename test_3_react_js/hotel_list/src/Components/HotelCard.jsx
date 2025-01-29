import React, { Component } from "react";

class HotelCard extends Component {
  render() {
    const { name, stars, address, boardbases, amenities, image } = this.props;
    return (
      <div className="bg-[#ffffff] rounded-2xl p-[20px] text-gray-900">
        <div className="mb-2">
          <div className="flex flex-row justify-between items-center mb-1">
            <div className="text-3xl text-[#003b95] font-[700]">{name}</div>
            <div className="bg-[#003b95] rounded-[10px] p-2">
              {"⭐".repeat(stars)}
            </div>
          </div>

          <hr />

          <div className="text-[20px] mb-4">{address}</div>
        </div>
        <div className="flex flex-row gap-5">
          <div className="max-w-[300px]">
            <img
              src={image}
              alt=""
              className="rounded-lg object-cover h-52 w-full aspect-16/9"
            />
          </div>
          <div className=" w-full">
            {boardbases.map((boardbase) => (
              <div className="text-xl">{boardbase}</div>
            ))}

            <hr />

            <div className="grid grid-cols-2 gap-2 items-center w-4/5 mt-4">
              {amenities.map((amenity) => (
                <div>· {amenity.name}</div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default HotelCard;
