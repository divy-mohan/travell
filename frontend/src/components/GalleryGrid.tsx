export interface GalleryImageData {
  id: number;
  image: string;
  seo_caption?: string;
}

export default function GalleryGrid({ images }: { images: GalleryImageData[] }) {
  if (!images || images.length === 0) return null;

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-4 max-w-7xl mx-auto">
      {images.map((img, index) => {
        // Create a simple masonry effect using span-rows dynamically
        const isTall = index % 3 === 0;
        const isWide = index % 5 === 0;
        
        return (
          <div 
            key={img.id} 
            className={`
              relative overflow-hidden rounded-xl shadow-sm hover:shadow-lg transition-shadow group
              ${isTall ? "col-span-2 row-span-2 md:col-span-1 md:row-span-2 h-64 md:h-80" : "h-40 md:h-48"}
              ${isWide && !isTall ? "col-span-2 md:col-span-2" : "col-span-1"}
            `}
          >
            <img
              src={img.image}
              alt={img.seo_caption || "Travel Destination"}
              className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
              loading="lazy"
            />
            {/* Hover Overlay */}
            <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center p-4 text-center">
              <span className="text-white font-medium drop-shadow-md">
                {img.seo_caption || "View Image"}
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
}
