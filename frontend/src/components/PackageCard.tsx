import Link from "next/link";
import Image from "next/image";

export interface PackageData {
  id: number;
  slug: string;
  title: string;
  description: string;
  image?: string;
  price?: number;
  focus_keyword?: string;
}

export default function PackageCard({ pkg }: { pkg: PackageData }) {
  return (
    <div className="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 flex flex-col h-full">
      <div className="relative w-full h-64 overflow-hidden">
        {pkg.image ? (
          <img
            src={pkg.image}
            alt={pkg.focus_keyword || pkg.title}
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
          />
        ) : (
          <div className="w-full h-full bg-gray-200 flex items-center justify-center">
            <span className="text-gray-400 font-serif">No Image</span>
          </div>
        )}
      </div>
      
      <div className="p-6 flex flex-col flex-grow text-center">
        <h3 className="font-serif text-2xl font-bold text-text-dark mb-3">
          {pkg.title}
        </h3>
        <p className="text-text-light mb-6 flex-grow line-clamp-3">
          {pkg.description}
        </p>
        
        {pkg.price && (
          <div className="font-bold text-secondary text-xl mb-4">
            ₹{pkg.price}
          </div>
        )}

        <Link
          href={`/package/${pkg.slug}`}
          className="mt-auto block w-full py-3 border-2 border-primary text-primary font-semibold rounded-lg hover:bg-primary hover:text-white transition-colors"
        >
          View Details
        </Link>
      </div>
    </div>
  );
}
