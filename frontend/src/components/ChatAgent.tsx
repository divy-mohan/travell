"use client";

import { useEffect, useState } from "react";
import { usePathname } from "next/navigation";

interface AgentData {
  agent_name: string;
  theme_color: string;
  teaser_messages: string[];
  greeting_messages: string[];
  suggested_prompts: string[];
  agent_avatar?: string;
}

export default function ChatAgent() {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);
  const [data, setData] = useState<AgentData | null>(null);
  const [teaser, setTeaser] = useState<string | null>(null);

  useEffect(() => {
    // Generate a simple slug from the pathname to pass to API
    const slug = pathname === "/" ? "home" : pathname.replace("/", "");

    fetch(`http://127.0.0.1:8000/api/v1/agent/?page=${slug}`)
      .then((res) => res.json())
      .then((json: AgentData) => {
        setData(json);
        if (json.teaser_messages && json.teaser_messages.length > 0) {
          const randomTeaser = json.teaser_messages[Math.floor(Math.random() * json.teaser_messages.length)];
          setTeaser(randomTeaser);
        }
      })
      .catch((err) => console.error("Agent fetch err:", err));
  }, [pathname]);

  if (!data) return null; // Don't render if API fails or is loading

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col items-end">
      {/* Teaser Popup */}
      {!isOpen && teaser && (
        <div className="mb-4 bg-white text-text-dark px-4 py-2 rounded-2xl shadow-lg border border-gray-100 animate-bounce cursor-pointer"
             onClick={() => setIsOpen(true)}>
          {teaser}
        </div>
      )}

      {/* Floating Bubble */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-14 h-14 rounded-full shadow-2xl flex items-center justify-center text-white text-2xl transition-transform hover:scale-110 active:scale-95"
        style={{ backgroundColor: data.theme_color || "#6B4F3B" }}
      >
        {isOpen ? "✕" : "💬"}
      </button>

      {/* Chat Window */}
      {isOpen && (
        <div className="absolute bottom-20 right-0 w-80 bg-white shadow-2xl rounded-2xl overflow-hidden border border-gray-100 transform origin-bottom-right transition-all">
          <div className="p-4 text-white" style={{ backgroundColor: data.theme_color || "#6B4F3B" }}>
            <h4 className="font-bold">{data.agent_name}</h4>
          </div>
          <div className="p-4 h-64 overflow-y-auto bg-gray-50 flex flex-col space-y-4">
            <div className="bg-white p-3 rounded-xl shadow-sm self-start max-w-[85%] text-sm text-text-dark">
               {data.greeting_messages?.[0] || "Hello! How can I help you?"}
            </div>
            
            {/* Suggested Prompts */}
            <div className="mt-auto flex flex-wrap gap-2 pt-4">
              {data.suggested_prompts?.map((prompt, idx) => (
                <button key={idx} className="bg-blue-50 text-xs text-blue-600 px-3 py-1.5 rounded-full border border-blue-100 hover:bg-blue-100 transition-colors">
                  {prompt}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
