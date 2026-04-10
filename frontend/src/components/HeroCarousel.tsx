"use client";

import { useState, useEffect } from "react";
import Image from "next/image";

export interface HeroImage {
  id: number;
  image: string;
  alt_text?: string;
}

export default function HeroCarousel({ data }: { data: HeroImage[] }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    if (!data || data.length === 0) return;
    const interval = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % data.length);
    }, 5000);
    return () => clearInterval(interval);
  }, [data]);

  if (!data || data.length === 0) {
    return (
      <div className="w-full h-[80vh] bg-secondary/20 flex items-center justify-center">
        <h1 className="text-4xl font-serif text-primary">Neem Karoli Travellers</h1>
      </div>
    );
  }

  return (
    <div className="relative w-full h-[80vh] overflow-hidden">
      {data.map((hero, index) => (
        <div
          key={hero.id}
          className={`absolute inset-0 transition-opacity duration-1000 ${
            index === currentIndex ? "opacity-100 relative z-10" : "opacity-0 absolute z-0"
          }`}
        >
          <img
            src={hero.image}
            alt={hero.alt_text || "Hero Image"}
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-black/40" />
        </div>
      ))}
      
      <div className="absolute inset-0 z-20 flex flex-col items-center justify-center text-center px-4">
        <h1 className="text-5xl md:text-7xl font-serif text-white font-bold mb-6 drop-shadow-lg">
          Discover Spiritual Peace
        </h1>
        <p className="text-lg md:text-2xl text-white/90 mb-8 max-w-2xl font-light">
          Experience premium travel and thrilling safaris guided by experts.
        </p>
        <button className="bg-primary hover:bg-primary-hover text-white px-8 py-3 rounded-md text-lg transition-all shadow-lg hover:shadow-xl hover:scale-105 active:scale-95">
          Explore Packages
        </button>
      </div>

      <div className="absolute bottom-8 left-0 right-0 z-20 flex justify-center space-x-2">
        {data.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentIndex(index)}
            className={`w-3 h-3 rounded-full transition-colors ${
              index === currentIndex ? "bg-secondary" : "bg-white/50"
            }`}
          />
        ))}
      </div>
    </div>
  );
}
