
import ProfileSection from "@/components/ProfileSection";
import ChatSection from "@/components/ChatSection";

const Index = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Animated background elements */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-cyan-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse animation-delay-2000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-60 h-60 bg-teal-500 rounded-full mix-blend-multiply filter blur-xl opacity-10 animate-pulse animation-delay-4000"></div>
      </div>

      <div className="relative z-10">
        {/* Header Navigation */}
        <header className="py-6 px-6">
          <nav className="max-w-6xl mx-auto">
            <div className="flex space-x-8">
              <a href="#" className="text-cyan-400 border-b-2 border-cyan-400 pb-1 font-medium transition-colors hover:text-cyan-300">
                Main
              </a>
              <a href="#" className="text-slate-400 hover:text-white transition-colors font-medium">
                Resume
              </a>
              <a href="#" className="text-slate-400 hover:text-white transition-colors font-medium">
                Skills
              </a>
            </div>
          </nav>
        </header>

        {/* Profile Section */}
        <ProfileSection />

        {/* Chat Section */}
        <ChatSection />
      </div>
    </div>
  );
};

export default Index;
