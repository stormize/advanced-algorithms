import java.io.*;
import java.util.*;

class Vertex {
	Vertex() {
		this.weight = 0;
		this.children = new ArrayList<Integer>();
	}
	int maxFun;
	int weight;
	ArrayList<Integer> children;
}

class PlanParty {
	static Vertex[] ReadTree() throws IOException {
		InputStreamReader input_stream = new InputStreamReader(System.in);
		BufferedReader reader = new BufferedReader(input_stream);
		StreamTokenizer tokenizer = new StreamTokenizer(reader);

		tokenizer.nextToken();
		int vertices_count = (int) tokenizer.nval;

		Vertex[] tree = new Vertex[vertices_count];

		for (int i = 0; i < vertices_count; ++i) {
			tree[i] = new Vertex();
			tokenizer.nextToken();
			tree[i].weight = (int) tokenizer.nval;
		}

		for (int i = 1; i < vertices_count; ++i) {
			tokenizer.nextToken();
			int from = (int) tokenizer.nval;
			tokenizer.nextToken();
			int to = (int) tokenizer.nval;
			tree[from - 1].children.add(to - 1);
			tree[to - 1].children.add(from - 1);
		}

		return tree;
	}

	static void dfs(Vertex[] tree, int vertex, int parent) {
		for (int c : tree[vertex].children)
			if (c!= parent)
				dfs(tree, c, vertex);
		int Fun1 = tree[vertex].weight;
		int Fun2 = 0;
		for(int child: tree[vertex].children){
			if(child!=parent){
	Fun2 =Fun2+ tree[child].maxFun;
		for(int grandchild: tree[child].children){					if(grandchild!= child && grandchild!=parent){
						Fun1 =Fun1+ tree[grandchild].maxFun;
					}
				}
			}
		}
		tree[vertex].maxFun = Math.max(Fun1, Fun2);
	}

	static int MaxWeightIndependentTreeSubset(Vertex[] tree) {
		int L = tree.length;
		if (L == 0)return 0;
		dfs(tree, 0, -1);
		return tree[0].maxFun;
	}

	public static void main(String[] args) throws IOException {
	  // This is to avoid stack overflow issues
	  new Thread(null, new Runnable() {
					public void run() {
						try {
							new PlanParty().run();
						} catch(IOException e) {
						}
					}
				}, "1", 1 << 26).start();
	}

	public void run() throws IOException {
		Vertex[] tree = ReadTree();
		int weight = MaxWeightIndependentTreeSubset(tree);
		System.out.println(weight);
	}
}