import HeroCarousel, { HeroImage } from "@/components/HeroCarousel";
import PackageCard, { PackageData } from "@/components/PackageCard";
import GalleryGrid, { GalleryImageData } from "@/components/GalleryGrid";

// Disable Next.js aggressive caching for these dynamic endpoints
export const revalidate = 60; 

async function getHeroImages(): Promise<HeroImage[]> {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/home/hero-images/", { 
      next: { revalidate: 60 } 
    });
    if (!res.ok) return [];
    return res.json();
  } catch (e) {
    console.error("Hero Fetch Error", e);
    return [];
  }
}

async function getPackages(): Promise<PackageData[]> {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/safari-packages/", { 
      next: { revalidate: 60 } 
    });
    if (!res.ok) return [];
    return res.json();
  } catch (e) {
    console.error("Packages Fetch Error", e);
    return [];
  }
}

async function getGalleryImages(): Promise<GalleryImageData[]> {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/home/gallery-images/", { 
      next: { revalidate: 60 } 
    });
    if (!res.ok) return [];
    return res.json();
  } catch (e) {
    console.error("Gallery Fetch Error", e);
    return [];
  }
}

export default async function Home() {
  const [heroData, packagesData, galleryData] = await Promise.all([
    getHeroImages(),
    getPackages(),
    getGalleryImages()
  ]);

  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <HeroCarousel data={heroData} />

      {/* Featured Packages Section */}
      <section className="py-24 bg-white">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-serif text-text-dark font-bold mb-4">
              Featured Journeys
            </h2>
            <div className="w-24 h-1 bg-secondary mx-auto mb-6"></div>
            <p className="text-text-light text-lg max-w-2xl mx-auto">
              Curated spiritual trips and wild encounters waiting for your arrival.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {packagesData.length > 0 ? (
              packagesData.map((pkg) => (
                <PackageCard key={pkg.id} pkg={pkg} />
              ))
            ) : (
              <div className="col-span-full text-center py-20 bg-gray-50 rounded-xl text-text-light border border-dashed border-gray-200">
                <p>No featured packages found. Ensure Django Server is running.</p>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Gallery Section */}
      <section className="py-24 bg-[#F9F7F3]">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-serif text-text-dark font-bold mb-4">
              Glimpses of Peace
            </h2>
            <div className="w-24 h-1 bg-secondary mx-auto mb-6"></div>
          </div>
          
          {galleryData.length > 0 ? (
            <GalleryGrid images={galleryData} />
          ) : (
            <div className="text-center py-20 bg-white rounded-xl shadow-sm text-text-light">
              <p>No gallery images uploaded yet.</p>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
