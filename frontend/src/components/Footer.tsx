import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-text-dark text-white pt-16 pb-8">
      <div className="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-12">
        <div>
          <h3 className="font-serif text-2xl mb-4 text-secondary">Neem Karoli Travellers</h3>
          <p className="text-gray-400">Guiding you through spiritual journeys and wild adventures with luxury and peace.</p>
        </div>
        <div>
          <h4 className="font-semibold text-lg mb-4">Quick Links</h4>
          <ul className="space-y-2 text-gray-400">
            <li><Link href="/" className="hover:text-secondary transition-colors">Home</Link></li>
            <li><Link href="/safaris" className="hover:text-secondary transition-colors">Safaris</Link></li>
            <li><Link href="/contact" className="hover:text-secondary transition-colors">Contact</Link></li>
          </ul>
        </div>
        <div>
          <h4 className="font-semibold text-lg mb-4">Contact Info</h4>
          <ul className="space-y-2 text-gray-400">
            <li>📍 123 Travel Road, India</li>
            <li>📞 +91 12345 67890</li>
            <li>✉️ info@neemkarolitravellers.com</li>
          </ul>
        </div>
      </div>
      <div className="container mx-auto px-4 mt-12 pt-8 border-t border-gray-800 text-center text-gray-500 text-sm">
        <p>© {new Date().getFullYear()} Neem Karoli Travellers. All rights reserved.</p>
      </div>
    </footer>
  );
}
