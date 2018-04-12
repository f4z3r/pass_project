#include "souffle/CompiledSouffle.h"

namespace souffle {
using namespace ram;
class Sf_reachable : public SouffleProgram {
private:
static inline bool regex_wrapper(const std::string& pattern, const std::string& text) {
   bool result = false; 
   try { result = std::regex_match(text, std::regex(pattern)); } catch(...) { 
     std::cerr << "warning: wrong pattern provided for match(\"" << pattern << "\",\"" << text << "\")\n";
}
   return result;
}
static inline std::string substr_wrapper(const std::string& str, size_t idx, size_t len) {
   std::string result; 
   try { result = str.substr(idx,len); } catch(...) { 
     std::cerr << "warning: wrong index position provided by substr(\"";
     std::cerr << str << "\"," << (int32_t)idx << "," << (int32_t)len << ") functor.\n";
   } return result;
}
public:
// -- initialize symbol table --
SymbolTable symTable
{
	"n0",
	"n1",
	"n2",
	"n3",
	"n4",
};// -- Table: Edge
ram::Relation<Auto,2>* rel_1_Edge;
// -- Table: Reachable
ram::Relation<Auto,2, ram::index<0,1>>* rel_2_Reachable;
souffle::RelationWrapper<0,ram::Relation<Auto,2, ram::index<0,1>>,Tuple<RamDomain,2>,2,false,true> wrapper_rel_2_Reachable;
// -- Table: @delta_Reachable
ram::Relation<Auto,2, ram::index<0>>* rel_3_delta_Reachable;
// -- Table: @new_Reachable
ram::Relation<Auto,2, ram::index<0>>* rel_4_new_Reachable;
public:
Sf_reachable() : rel_1_Edge(new ram::Relation<Auto,2>()),
rel_2_Reachable(new ram::Relation<Auto,2, ram::index<0,1>>()),
wrapper_rel_2_Reachable(*rel_2_Reachable,symTable,"Reachable",std::array<const char *,2>{{"s:Node","s:Node"}},std::array<const char *,2>{{"n","m"}}),
rel_3_delta_Reachable(new ram::Relation<Auto,2, ram::index<0>>()),
rel_4_new_Reachable(new ram::Relation<Auto,2, ram::index<0>>()){
addRelation("Reachable",&wrapper_rel_2_Reachable,0,1);
}
~Sf_reachable() {
delete rel_1_Edge;
delete rel_2_Reachable;
delete rel_3_delta_Reachable;
delete rel_4_new_Reachable;
}
private:
template <bool performIO> void runFunction(std::string inputDirectory = ".", std::string outputDirectory = ".") {
SignalHandler::instance()->set();
// -- initialize counter --
std::atomic<RamDomain> ctr(0);

#if defined(__EMBEDDED_SOUFFLE__) && defined(_OPENMP)
omp_set_num_threads(1);
#endif

// -- query evaluation --
SignalHandler::instance()->setMsg(R"_(Edge("n0","n1").
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [8:1-8:17])_");
rel_1_Edge->insert(RamDomain(0),RamDomain(1));
SignalHandler::instance()->setMsg(R"_(Edge("n1","n2").
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [9:1-9:17])_");
rel_1_Edge->insert(RamDomain(1),RamDomain(2));
SignalHandler::instance()->setMsg(R"_(Edge("n2","n3").
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [10:1-10:17])_");
rel_1_Edge->insert(RamDomain(2),RamDomain(3));
SignalHandler::instance()->setMsg(R"_(Edge("n1","n4").
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [11:1-11:17])_");
rel_1_Edge->insert(RamDomain(1),RamDomain(4));
SignalHandler::instance()->setMsg(R"_(Reachable(x,y) :- 
   Edge(x,y).
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [21:1-21:29])_");
if (!rel_1_Edge->empty()) {
auto part = rel_1_Edge->partition();
PARALLEL_START;
CREATE_OP_CONTEXT(rel_1_Edge_op_ctxt,rel_1_Edge->createContext());
CREATE_OP_CONTEXT(rel_2_Reachable_op_ctxt,rel_2_Reachable->createContext());
pfor(auto it = part.begin(); it<part.end(); ++it) 
try{for(const auto& env0 : *it) {
Tuple<RamDomain,2> tuple({{(RamDomain)(env0[0]),(RamDomain)(env0[1])}});
rel_2_Reachable->insert(tuple,READ_OP_CONTEXT(rel_2_Reachable_op_ctxt));
}
} catch(std::exception &e) { SignalHandler::instance()->error(e.what());}
PARALLEL_END;
}
SignalHandler::instance()->setMsg(R"_(Reachable(x,x) :- 
   Edge(x,_).
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [24:1-24:29])_");
if (!rel_1_Edge->empty()) {
auto part = rel_1_Edge->partition();
PARALLEL_START;
CREATE_OP_CONTEXT(rel_1_Edge_op_ctxt,rel_1_Edge->createContext());
CREATE_OP_CONTEXT(rel_2_Reachable_op_ctxt,rel_2_Reachable->createContext());
pfor(auto it = part.begin(); it<part.end(); ++it) 
try{for(const auto& env0 : *it) {
Tuple<RamDomain,2> tuple({{(RamDomain)(env0[0]),(RamDomain)(env0[0])}});
rel_2_Reachable->insert(tuple,READ_OP_CONTEXT(rel_2_Reachable_op_ctxt));
}
} catch(std::exception &e) { SignalHandler::instance()->error(e.what());}
PARALLEL_END;
}
SignalHandler::instance()->setMsg(R"_(Reachable(y,y) :- 
   Edge(_,y).
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [25:1-25:29])_");
if (!rel_1_Edge->empty()) {
auto part = rel_1_Edge->partition();
PARALLEL_START;
CREATE_OP_CONTEXT(rel_1_Edge_op_ctxt,rel_1_Edge->createContext());
CREATE_OP_CONTEXT(rel_2_Reachable_op_ctxt,rel_2_Reachable->createContext());
pfor(auto it = part.begin(); it<part.end(); ++it) 
try{for(const auto& env0 : *it) {
Tuple<RamDomain,2> tuple({{(RamDomain)(env0[1]),(RamDomain)(env0[1])}});
rel_2_Reachable->insert(tuple,READ_OP_CONTEXT(rel_2_Reachable_op_ctxt));
}
} catch(std::exception &e) { SignalHandler::instance()->error(e.what());}
PARALLEL_END;
}
rel_3_delta_Reachable->insertAll(*rel_2_Reachable);
for(;;) {
SignalHandler::instance()->setMsg(R"_(Reachable(x,y) :- 
   Edge(x,z),
   Reachable(z,y).
in file /Users/jakob_beckmann/Documents/_uni/eth/_courses/2018/spring/program_analysis_for_system_security_and_reliability/pass_project/souffle_tests/reachable.dl [28:1-28:45])_");
if (!rel_3_delta_Reachable->empty()&&!rel_1_Edge->empty()) {
auto part = rel_1_Edge->partition();
PARALLEL_START;
CREATE_OP_CONTEXT(rel_3_delta_Reachable_op_ctxt,rel_3_delta_Reachable->createContext());
CREATE_OP_CONTEXT(rel_4_new_Reachable_op_ctxt,rel_4_new_Reachable->createContext());
CREATE_OP_CONTEXT(rel_1_Edge_op_ctxt,rel_1_Edge->createContext());
CREATE_OP_CONTEXT(rel_2_Reachable_op_ctxt,rel_2_Reachable->createContext());
pfor(auto it = part.begin(); it<part.end(); ++it) 
try{for(const auto& env0 : *it) {
const Tuple<RamDomain,2> key({{env0[1],0}});
auto range = rel_3_delta_Reachable->equalRange<0>(key,READ_OP_CONTEXT(rel_3_delta_Reachable_op_ctxt));
for(const auto& env1 : range) {
if( !rel_2_Reachable->contains(Tuple<RamDomain,2>({{env0[0],env1[1]}}),READ_OP_CONTEXT(rel_2_Reachable_op_ctxt))) {
Tuple<RamDomain,2> tuple({{(RamDomain)(env0[0]),(RamDomain)(env1[1])}});
rel_4_new_Reachable->insert(tuple,READ_OP_CONTEXT(rel_4_new_Reachable_op_ctxt));
}
}
}
} catch(std::exception &e) { SignalHandler::instance()->error(e.what());}
PARALLEL_END;
}
if(rel_4_new_Reachable->empty()) break;
rel_2_Reachable->insertAll(*rel_4_new_Reachable);
{
auto rel_0 = rel_3_delta_Reachable;
rel_3_delta_Reachable = rel_4_new_Reachable;
rel_4_new_Reachable = rel_0;
}
rel_4_new_Reachable->purge();
}
if (!isHintsProfilingEnabled() && (performIO || 1)) rel_3_delta_Reachable->purge();
if (!isHintsProfilingEnabled() && (performIO || 1)) rel_4_new_Reachable->purge();
if (performIO) {
try {std::map<std::string, std::string> directiveMap({{"IO","stdout"},{"attributeNames","n\tm"},{"name","Reachable"}});
if (!outputDirectory.empty() && directiveMap["IO"] == "file" && directiveMap["filename"].front() != '/') {directiveMap["filename"] = outputDirectory + "/" + directiveMap["filename"];}
IODirectives ioDirectives(directiveMap);
IOSystem::getInstance().getWriter(SymbolMask({1, 1}), symTable, ioDirectives, 0)->writeAll(*rel_2_Reachable);
} catch (std::exception& e) {std::cerr << e.what();exit(1);}
}
if (!isHintsProfilingEnabled() && (performIO || 0)) rel_1_Edge->purge();
if (!isHintsProfilingEnabled() && (performIO || 0)) rel_2_Reachable->purge();

// -- relation hint statistics --
if(isHintsProfilingEnabled()) {
std::cout << " -- Operation Hint Statistics --\n";
std::cout << "Relation rel_1_Edge:\n";
rel_1_Edge->printHintStatistics(std::cout,"  ");
std::cout << "\n";
std::cout << "Relation rel_2_Reachable:\n";
rel_2_Reachable->printHintStatistics(std::cout,"  ");
std::cout << "\n";
std::cout << "Relation rel_3_delta_Reachable:\n";
rel_3_delta_Reachable->printHintStatistics(std::cout,"  ");
std::cout << "\n";
std::cout << "Relation rel_4_new_Reachable:\n";
rel_4_new_Reachable->printHintStatistics(std::cout,"  ");
std::cout << "\n";
}
SignalHandler::instance()->reset();
}
public:
void run() override { runFunction<false>(); }
public:
void runAll(std::string inputDirectory = ".", std::string outputDirectory = ".") override { runFunction<true>(inputDirectory, outputDirectory); }
public:
void printAll(std::string outputDirectory = ".") override {
try {std::map<std::string, std::string> directiveMap({{"IO","stdout"},{"attributeNames","n\tm"},{"name","Reachable"}});
if (!outputDirectory.empty() && directiveMap["IO"] == "file" && directiveMap["filename"].front() != '/') {directiveMap["filename"] = outputDirectory + "/" + directiveMap["filename"];}
IODirectives ioDirectives(directiveMap);
IOSystem::getInstance().getWriter(SymbolMask({1, 1}), symTable, ioDirectives, 0)->writeAll(*rel_2_Reachable);
} catch (std::exception& e) {std::cerr << e.what();exit(1);}
}
public:
void loadAll(std::string inputDirectory = ".") override {
}
public:
void dumpInputs(std::ostream& out = std::cout) override {
}
public:
void dumpOutputs(std::ostream& out = std::cout) override {
try {IODirectives ioDirectives;
ioDirectives.setIOType("stdout");
ioDirectives.setRelationName("rel_2_Reachable");
IOSystem::getInstance().getWriter(SymbolMask({1, 1}), symTable, ioDirectives, 0)->writeAll(*rel_2_Reachable);
} catch (std::exception& e) {std::cerr << e.what();exit(1);}
}
public:
const SymbolTable &getSymbolTable() const override {
return symTable;
}
};
SouffleProgram *newInstance_reachable(){return new Sf_reachable;}
SymbolTable *getST_reachable(SouffleProgram *p){return &reinterpret_cast<Sf_reachable*>(p)->symTable;}
#ifdef __EMBEDDED_SOUFFLE__
class factory_Sf_reachable: public souffle::ProgramFactory {
SouffleProgram *newInstance() {
return new Sf_reachable();
};
public:
factory_Sf_reachable() : ProgramFactory("reachable"){}
};
static factory_Sf_reachable __factory_Sf_reachable_instance;
}
#else
}
int main(int argc, char** argv)
{
try{
souffle::CmdOptions opt(R"(reachable.dl)",
R"(.)",
R"(.)",
false,
R"()",
1
);
if (!opt.parse(argc,argv)) return 1;
#if defined(_OPENMP) 
omp_set_nested(true);
#endif
souffle::Sf_reachable obj;
obj.runAll(opt.getInputFileDir(), opt.getOutputFileDir());
return 0;
} catch(std::exception &e) { souffle::SignalHandler::instance()->error(e.what());}
}
#endif
