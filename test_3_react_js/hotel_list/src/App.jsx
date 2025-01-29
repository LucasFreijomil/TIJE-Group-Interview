import React, { Component } from "react";
import axios from "axios";
import HotelCard from "./Components/HotelCard";

class App extends Component {
  state = {
    hotels: [],
  };

  async fetchHotels() {
    try {
      const { data } = await axios.get(
        "https://wmw3lg8sha.execute-api.us-east-2.amazonaws.com/dev/dummy"
      );
      const hotels = data.data.hotels;
      this.setState({ hotels: hotels });
      console.log(this.state.hotels);
    } catch (error) {
      console.log(error);
    }
  }

  componentDidMount() {
    this.fetchHotels();
  }
  
  render() {
    return (
      <div className="flex flex-col justify-center items-center my-10">
        <div className=" max-w-[896px]  w-[80%] flex flex-col gap-10">
          {this.state.hotels.map((hotel) => (
            <HotelCard
              name={hotel.name}
              stars={hotel.stars}
              address={hotel.address}
              boardbases={hotel.boardbases}
              amenities={hotel.amenities}
              image={hotel.image}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default App;
